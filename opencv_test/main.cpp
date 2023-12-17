#include <iostream>
#include <opencv2/opencv.hpp>

int main(int, char**) {
    cv::Mat image;
    image = cv::imread("D:\\Programming\\lena.png");
    if(!image.data) {
        std::cout << "No image data." << std::endl;
        return -1;
    }
    std::cout << "Values of attributes about the image\n";
    std::cout << "No of Rows = " << image.rows << std::endl;
    std::cout << "No of Columns = " << image.cols << std::endl;
    std::cout << "Matrix type = " << image.type() << std::endl;
    std::cout << "No of Channels = " << image.channels() << std::endl;
    std::cout << "Total no of Elements = " << image.total() << std::endl;
    std::cout << "Rows element in bytes: " << image.step[0] << std::endl;
    std::cout << "Columns element in bytes: " << image.step[1] << std::endl;
    cv::namedWindow("Display Image", cv::WINDOW_AUTOSIZE);
    cv::imshow("Display Image", image);
    cv::waitKey(0);
}
