import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
import os

def generate_launch_description():
    # 获取包的共享目录路径
    package_share_directory = get_package_share_directory('my_pkg')

    # 拼接 params.yaml 配置文件的路径
    config_file_path = os.path.join(package_share_directory, 'config', 'params.yaml')

    print(f"Config file path: {config_file_path}")  # 打印配置文件路径

    return LaunchDescription([

        # 声明启动时的配置文件路径参数
        DeclareLaunchArgument(
            'config_file',
            default_value=config_file_path,
            description='Path to the parameter file'
        ),

        # 启动节点并加载参数文件
        Node(
            package='my_pkg',  # 你的包名
            executable='my_node',  # 你的可执行文件名
            name='my_node',  # 节点名称
            output='screen',
            parameters=[LaunchConfiguration('config_file')],  # 加载配置文件路径作为参数
        ),

        # 打印日志确认节点启动
        LogInfo(
            msg="Starting with parameter file"
        )
    ])


