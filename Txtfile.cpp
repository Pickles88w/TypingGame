#include <iostream>
#include <fstream>
#include <vector>
#include <string>

int main() {
    std::vector<std::string> words = {
        "apple", "mystery", "journey", "ocean", "pyramid",
        "echo", "rainbow", "rhythm", "wizard", "labyrinth",
        "galaxy", "volcano", "whisper", "zigzag", "melody",
        "quartz", "jigsaw", "horizon", "eclipse", "bamboo",
        "pixel", "whirlwind", "zenith", "avalanche", "mosaic"
    };

    std::ofstream outFile("words.txt");
    if (!outFile) {
        std::cerr << "Error opening file for writing." << std::endl;
        return 1;
    }

    for (const auto& word : words) {
        outFile << word << "\n";
    }

    outFile.close();
    std::cout << "Words list saved to words.txt" << std::endl;

    return 0;
}
