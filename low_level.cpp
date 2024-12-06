// Code réalisé par Thibault Flavie et Ferré Aurélien

#include <Eigen/Dense>
#include <chrono>
#include <cpr/cpr.h>
#include <fstream>
#include <iostream>
#include <nlohmann/json.hpp>

int main() {

  // Récupération d'une tâche depuis le proxy
  std::string url = "http://localhost:8000";
  cpr::Response r = cpr::Get(cpr::Url{url});

  if (r.status_code != 200) {
    std::cerr << "Erreur lors de la requête : " << r.status_code << std::endl;
    return 1;
  }

  try {
    nlohmann::json data = nlohmann::json::parse(r.text);

    // Extraire les données "a" et "b" et "id"
    std::vector<std::vector<double>> a =
        data["a"].get<std::vector<std::vector<double>>>();
    std::vector<double> b = data["b"].get<std::vector<double>>();
    int id = data["identifier"].get<int>();

    std::cout << std::fixed << std::setprecision(15);

    size_t n = a.size();
    size_t m = b.size();

    if (n == 0 || a[0].size() != m) {
      std::cerr << "Erreur : les dimensions de la matrice et du vecteur ne "
                   "correspondent pas."
                << std::endl;
      return 1;
    }

    // Création d'une matrice à partir de a
    int rows = a.size();
    int cols = a[0].size();
    Eigen::MatrixXd mata(rows, cols);

    // Remplir la matrice Eigen avec les données de a
    for (int i = 0; i < rows; ++i) {
      for (int j = 0; j < cols; ++j) {
        mata(i, j) = a[i][j];
      }
    }

    // Création d'un vecteur à partir de b
    Eigen::VectorXd b_eigen(b.size());
    for (size_t i = 0; i < b.size(); ++i) {
      b_eigen(i) = b[i];
    }

    // Résolution de mesure temporelle du problème
    auto start = std::chrono::high_resolution_clock::now();
    Eigen::VectorXd x = mata.llt().solve(b_eigen);
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;

    std::cout << "Task " << id << " réalisée en " << duration.count()
              << " secondes." << std::endl;

    // Création de l'objet JSON à renvoyer au proxy
    nlohmann::json result_json;
    result_json["a"] = a;
    result_json["b"] = b;
    result_json["x"] = x;
    result_json["time"] = duration.count();
    result_json["identifier"] = id;
    std::string result_payload = result_json.dump();

    // Requête POST sur le proxy
    cpr::Response post_response = cpr::Post(
        cpr::Url{url}, cpr::Header{{"Content-Type", "application/json"}},
        cpr::Body{result_payload});

    // Vérifier le statut de la requête POST
    if (post_response.status_code != 200) {
      std::cerr << "Erreur lors de la requête POST : "
                << post_response.status_code << std::endl;
      std::cerr << "Message : " << post_response.text << std::endl;
      return 1;
    }

  } catch (const std::exception &e) {
    std::cerr << "Erreur de parsing JSON : " << e.what() << std::endl;
    return 1;
  }

  return 0;
}
