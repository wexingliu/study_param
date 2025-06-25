import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
import os

def generate_launch_description():
    current_dir = os.getcwd()  # 获取当前工作目录
    print(f"Current directory: {current_dir}")  # 打印当前目录

    return LaunchDescription([

        # 启动节点并加载参数文件
        Node(
            package='my_pkg',  # 你的包名
            executable='my_node',  # 你的可执行文件名
            name='my_node',  # 节点名称
            output='screen',
            parameters=[
                '/home/liuux/1demo/code/study_param/src/my_pkg/config/params.yaml',
            ],
        ),

        # 打印日志确认节点启动
        LogInfo(
            msg="Starting with default parameter file"
        )
    ])

