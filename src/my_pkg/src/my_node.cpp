#include <iostream>
#include <rclcpp/rclcpp.hpp>

class MyNode : public rclcpp::Node
{
public:
  MyNode() : Node("my_node")
  {
    std::cout << "node..." << std::endl;

    // 声明参数并提供默认值
    this->declare_parameter<std::string>("greeting", "Hello");
    this->declare_parameter<std::string>("name", "ROS2");
    this->declare_parameter<int>("ExposureTime", 50000);

    // 获取参数
    std::string greeting = this->get_parameter("greeting").as_string();
    std::string name     = this->get_parameter("name").as_string();
    int ExposureTime     = this->get_parameter("ExposureTime").as_int();

    // 打印信息
    std::cout << greeting << ", " << name << std::endl;
    std::cout << "ExposureTime: " << ExposureTime << std::endl;
  }

  ~MyNode()
  {
    std::cout << "bye..." << std::endl;
  }
};

int main(int argc, char ** argv)
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<MyNode>());
    rclcpp::shutdown();
    return 0;
}
