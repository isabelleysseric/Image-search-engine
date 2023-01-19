#include <opencv2/opencv.hpp>
#include <iostream>
#include <vector>

int main() {
    // Load the reference images
    std::vector<cv::Mat> reference_images;
    for (int i = 1; i <= n; i++) {
        reference_images.push_back(cv::imread("reference_image_" + std::to_string(i) + ".jpg"));
    }

    // Load the input image
    cv::Mat input_image = cv::imread("input_image.jpg");

    // Initialize variables to keep track of the best match
    double best_match = 0;
    int best_match_index = -1;

    // Compare the input image to each reference image
    for (int i = 0; i < reference_images.size(); i++) {
        // Resize the images to the same size
        cv::resize(input_image, input_image, reference_images[i].size());

        // Compute the mean squared error (MSE) between the images
        cv::Scalar mse = cv::norm(input_image, reference_images[i], cv::NORM_L2SQR);

        // Check if this is the best match so far
        if (mse[0] > best_match) {
            best_match = mse[0];
            best_match_index = i;
        }
    }

    // Print the index of the best matching image
    std::cout << "Best matching image: " << best_match_index << std::endl;

    return 0;
}
