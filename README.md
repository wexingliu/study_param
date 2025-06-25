# study_param





```
ros2 pkg create my_pkg --build-type ament_cmake --dependencies rclcpp --node-name my_node
```









`liuux@liuux:~/1demo/code/study_param$ ros2 param list
/my_node:
  ExposureTime
  greeting
  name
  qos_overrides./parameter_events.publisher.depth
  qos_overrides./parameter_events.publisher.durability
  qos_overrides./parameter_events.publisher.history
  qos_overrides./parameter_events.publisher.reliability
  use_sim_time
liuux@liuux:~/1demo/code/study_param$ ros2 param get my_node name 
String value is: BUDING DUODUO
liuux@liuux:~/1demo/code/study_param$ ros2 param get my_node greeting
String value is: Hello`





`liuux@liuux:~/1demo/code/study_param$ ros2 param get my_node ExposureTime
Integer value is: 12345
liuux@liuux:~/1demo/code/study_param$ ros2 param set my_node ExposureTime 666
Set parameter successful
liuux@liuux:~/1demo/code/study_param$ ros2 param get my_node ExposureTime
Integer value is: 666`



`liuux@liuux:~/1demo/code/study_param$ ros2 param get my_node ExposureTime
Integer value is: 12345
liuux@liuux:~/1demo/code/study_param$ ros2 param set my_node ExposureTime 666
Set parameter successful
liuux@liuux:~/1demo/code/study_param$ ros2 param dump my_node
/my_node:
  ros__parameters:
    ExposureTime: 666
    greeting: Hello
    name: BUDING DUODUO
    qos_overrides:
      /parameter_events:
        publisher:
          depth: 1000
          durability: volatile
          history: keep_last
          reliability: reliable
    use_sim_time: false`



`liuux@liuux:~/1demo/code/study_param$ ros2 param describe my_node greeting
Parameter name: greeting
  Type: string
  Constraints:`











# ros2   参数Param



一、什么是参数

参数类似ROS中的全局字典，多个节点可以共享参数中的数据。
参数在ROS中以键-值对的形式存储，即字典中的一个名目对应一个值，可以通过访问参数名来获取参数值
在ROS2中，参数属于节点，存储在节点中




ROS2 param下的命令有七条

```cpp
  delete    Delete parameter
  describe  Show descriptive information about declared parameters
  dump      Dump the parameters of a node to a yaml file
  get       Get parameter
  list      Output a list of available parameters
  load      Load parameter file for a node
  set       Set parameter
```



- **delete** - 删除参数
- **describe** - 显示已声明参数的描述信息
- **dump** - 将节点的参数导出到 YAML 文件
- **get** - 获取参数
- **list** - 输出可用参数的列表
- **load** - 为节点加载参数文件
- **set** - 设置参数









## ros2 param list

输出当前的Param表，每个节点名后面跟的是这个节点的参数



```bash
ros2 param list
```



##  ros2 param get

输出节点Node的参数Param的数据类型Type以及它的值Value

```bash
ros2 param get <node_name> <parameter_name>
```





##  ros2 param set

设置参数值

```plain
ros2 param set <node_name> <parameter_name> <value>
```

以修改海龟背景色为例

```plain
ros2 param set /turtlesim background_r 150
OUTPUT:
Set parameter successful
```

##  ros2 param dump

将节点Node的参数Param存储到文件

```plain
ros2 param dump <node_name>
```

以保存海龟节点的参数信息为例，将会自动保存到当前工作目录（存疑，因为没有找到）

```plain
ros2 param dump /turtlesim
OUTPUT:
/turtlesim:
  ros__parameters:
    background_b: 255
    background_g: 86
    background_r: 150
    qos_overrides:
      /parameter_events:
        publisher:
          depth: 1000
          durability: volatile
          history: keep_last
          reliability: reliable
    use_sim_time: false
```

保存到指定位置（但当前命令已经弃用，提示使用重定向）

```plain
ros2 param dump /turtlesim --output-dir /home/ubuntu2204/turtle_ws
```

## ros2 param load

加载参数文件

```plain
ros2 param load <node_name> <parameter_file>
```

以加载海龟的配置参数文件为例

```plain
ros2 param load /turtlesim /home/ubuntu2204/turtle_ws/turtlesim.yaml
```

因为只读参数只能在程序启动时修改，运行后不得修改，所以此处报错
**在启动节点时一并加载相应的参数文件：**

```plain
ros2 run <package_name> <executable_name> --ros-args --params-file <file_name>
ros2 run turtlesim turtlesim_node --ros-args --params-file /home/ubuntu2204/turtle_ws/turtlesim.yaml
```

此时成功加载文件，并且不会报只读参数的错

## ros2 param delete

删除节点的某个参数

```plain
ros2 param delete <node_name> <parameter_name>
```

## ros2 param describe

展示某个参数的描述性信息，这部分属于ros2新加的内容，一般参数都没有说明

```bash
ros2 param describe <node_name> <parameter_name>
```









# 2 如何 配置使用参数 和 配置 configs.yaml

config.yaml 的作用在我看来就是可以统一的管理所有参数的默认值，比较方便



2.1 cpp 内创建参数和得到参数



declare_parameter<int>("param_01", 1); // 声明并初始化参数

get_parameter("param_01", param_01);   // 参数的值赋给变量 param_01



这样写就默认会被 ROS2 检测到这个参数，并且各种命令都是可以使用的，通过命令改变参数的值是直接影响到程序中的,此外，本文的下面都是以参数 “param_01” 举例的



2.2 创建 configs.yaml

功能包目录下创建 configs/config.yaml 名字其实无所谓，通常为了规范阅读默认起这个名字

config.yaml 文件格式要这样写：



```bash
/Template:            #可执行文件名称，也就是 CMakeList 里 add_executable()函数定义的可执行文件
	ros__parameters:  #固定格式，要加这几句话
		param_01: 123456    #参数名称，冒号，空格，值；
		use_sim_time: false #注意:参数要在节点里面创建好
```







**2.****.3 使用 config.yaml 文件**



2.3.1 命令行启动

运行节点时候运行 config.yaml 文件



ros2 run <package_name> <executable_name> --ros-args --params-file <file_name>  
ros2 run Template Template --ros-args --params-file ./src/Template/configs/config.yaml    





运行节点后运行 config.yaml 文件



ros2 param load <node_name> <parameter_file>   

ros2 param load /Template ./src/Template/configs/config.yaml



**2.3.2 Launch 文件启动**



\1. 配置 CMakeLists.txt 文件

在 CMakeLists.txt 里面导入 configs.yaml 文件



```bash
install(FILES configs/config.yaml
DESTINATION share/${PROJECT_NAME}/configs)
```

\-------------------------------------------------------------------------------------------------------------------------------------------



✅ 含义：

- `install(...)`：CMake 的安装命令，用于指定哪些文件/目录应该在 `colcon install` 或 `cmake --install` 阶段被复制。
- `FILES`：表示你要安装的是单个或多个**文件**（不是目录）。
- `configs/config.yaml`：表示要被安装的原始文件路径（相对于 CMakeLists.txt）。
- `DESTINATION`：指定安装目标目录的相对路径。
- `share/${PROJECT_NAME}/configs`：表示将文件安装到 `install/share/<项目名>/configs` 目录下。

- - `${PROJECT_NAME}` 会自动被替换为 `project(<name>)` 中设置的项目名称。

------

📁 安装后的文件路径示例

假设你的项目叫 `unitree_controller`，安装后你会在 ROS 2 安装空间中看到：

```cmake
install/share/unitree_controller/configs/config.yaml
```





DIRECTORY     指定要安装的是一个目录，而不是单个文件。

\-------------------------------------------------------------------------------------------------------------------------------------------





**2.3.3 配置 Launch 文件**



绝对路径配置 Launch 文件

在 Launch 文件启动节点那个下面再加几行代码

```bash
parameters=[
	'/home/ice/Template_ICE/src/Template/configs/config.yaml',
],   # 这个是绝对路径，移植性比较差，较为简单
```



完整代码：

```bash
Node(
	package='Template',
	executable='Template',
	name='Template',
	output='screen',
	parameters=[
		'/home/ice/Template_ICE/src/Template/configs/config.yaml',
	],
 ),	
```





**相对路径配置 Launch 文件**

使用函数 get_package_share_directory() 来完成这个操作，这个函数是用来获取功能包的路径的



导入 get_package_share_directory 库



from ament_index_python.packages import get_package_share_directory



使用 get_package_share_directory() 这个函数获得包的路径并保存在一个变量里面



Template_pkg_share_dir = get_package_share_directory('Template')  # 等号前面的是变量名



这行代码我放在了这里

![img](https://cdn.nlark.com/yuque/0/2025/png/43772131/1750784808134-3856ad20-4c99-480f-a956-64c3bd8a5a59.png)

在 Launch 文件启动节点那个下面再加几行代码



parameters=[

​	Template_pkg_share_dir + '/configs/config.yaml', 

\# 这块的 Template_pkg_share_dir 是我上面定义的那个变量  

],





```bash
Node(
	package='Template',
	executable='Template',
	name='Template',
	output='screen',
	parameters=[
		Template_pkg_share_dir + '/configs/config.yaml',
	],
 ),	
```



**三. Launch 文件不使用 config.yaml 文件操控参数值**



在 Launch 文件启动节点那个下面再加几行代码

```bash
 parameters=[
	{
		"param_01": 567,
		"use_sim_time": False,
	}
],
```



完整代码:

```bash
Node(
	package='Template',
	executable='Template',
	name='Template',
	output='screen',
	parameters=[
		{
			"param_01": 567,
			"use_sim_time": False,
		}
	],
 ),	
```























