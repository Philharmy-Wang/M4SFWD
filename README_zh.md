# 1. MSFFD下载地址
我们提供了两种方式来获取MSFFD：

  - **Roboflow**，本数据集的地址为:https://universe.roboflow.com/yunnan-university/synthetic-fire-smoke

  - **云端硬盘**，我们针对不同的目标检测算法（coco, darknet, yolov6, yolov7, yolov8），提供了不同标注格式的数据.

      - **谷歌云盘**的下载链接为：
          - [**coco**](https://drive.google.com/file/d/12iLl-uDIrAuZ1-2vmbeP3bDcOQXB4Mds/view?usp=share_link), 

          - [**darknet**](https://drive.google.com/file/d/1wSjo9qVpwEntL9Olt_y7xrmH-0tuK8Fp/view?usp=share_link), 

          - [**yolov6**](https://drive.google.com/file/d/1FB7Pjnz0DqXvxVUcfvK2lwPZssUOQguH/view?usp=share_link), 

          - [**yolov7**](https://drive.google.com/file/d/1eVQ2OG1NXEHaheuTuTl6kPz7NlpEy9wx/view?usp=share_link),
 
          - [**yolov8**](https://drive.google.com/file/d/1VRJxqXZZibQap9TmL-z-caNJsnd5Y70q/view?usp=share_link), 

          - [**different_weather_and_time**](https://drive.google.com/file/d/1i5HDMOHKaDZNrGixJUGSSFJLgrrHZEb-/view?usp=share_link)。 

      - **百度云盘**的下载链接为：
      
         - **coco:**    https://pan.baidu.com/s/18w33GJtQar0gfOM3ocuR1A?pwd=yqv8 提取码：yqv8 

        - **darknet:**  https://pan.baidu.com/s/1jqzTn93ixUf_TXhrCRaW4w?pwd=c8dx 提取码：c8dx 

        - **yolov6:**   https://pan.baidu.com/s/1X_2mmSyAMCshnYJIOeQnYg?pwd=fk3r 提取码：fk3r 
  
        - **yolov7:**   https://pan.baidu.com/s/1HgC5YpEtF3VJgLt5zRD_Uw?pwd=q89a 提取码：q89a 

        - **yolov8:**   https://pan.baidu.com/s/1VDbQBMD3SamF0a7_r9aLow?pwd=2rsq 提取码：2rsq 

         - **different_weather_and_time:**  https://pan.baidu.com/s/1O4QKkeJubQa6lZKRdnwR6w?pwd=txil 提取码：txil 
  
# 2. 场景介绍
为了实现森林火灾的真实模拟，我们运用了虚幻引擎5来构建多样化的森林场景。

虚幻引擎5可满足现实世界中森林的地形、气象、时间、光影、纹理等细节，也可模拟不同时期的多尺度森林火灾，非常适合合成数据集的构建。

我们通过虚幻引擎5搭建了八个不同地形的场景，包含晴天、雾天和雨雪天三种气象条件，以及白天、傍晚和夜晚三个不同的时间。

下表为原始数据的详细信息。


|           |     Scenario    |     Resolution    |     FPS     |     Duration       |     Size        |     Weather      |     The number of objects    |     Description                                                 |
|-----------|-----------------|-------------------|-------------|--------------------|-----------------|------------------|------------------------------|-----------------------------------------------------------------|
|     1     |     a           |     1480×684      |     17.6    |     126 seconds    |     270.7 Mb    |     Sunny        |     Multiple Objects         |     Daylight, mountains, and plains                             |
|     2     |     a           |     1480×684      |     17.7    |     85 seconds     |     227.5 Mb    |     Sunny        |     No Objects               |     Evening, mountains, and plains                              |
|     3     |     a           |     1480×684      |     17.2    |     109 seconds    |     30.2 Mb     |     Sunny        |     Multiple Objects         |     Night, mountains, and plains                                |
|     4     |     a           |     1480×684      |     13.8    |     79 seconds     |     184.1 Mb    |     Sunny        |     No Objects               |     Evening, mountains, and plains                              |
|     5     |     a           |     776×452       |     18.6    |     113 seconds    |     75.3 Mb     |     Sunny        |     No Objects               |     Daylight, mountains, and plains                             |
|     6     |     a           |     1480×684      |     17.9    |     82 seconds     |     9.7 Mb      |     Sunny        |     Single Object            |     Night, mountains, and plains                                |
|     7     |     b           |     1480×684      |     29.9    |     115 seconds    |     496.2 Mb    |     Sunny        |     Multiple Objects         |     Daylight, mountains, and plains                             |
|     8     |     b           |     1480×684      |     28      |     82 seconds     |     314.4 Mb    |     Sunny        |     No Objects               |     Daylight, Evening, Night, mountains, and   plains           |
|     9     |     b           |     1480×684      |     29.9    |     101 seconds    |     477.4 Mb    |     Sunny        |     Single Object            |     Daylight, mountains, and plains                             |
|     10    |     b           |     1480×684      |     26.5    |     83 seconds     |     43.4 Mb     |     Sunny        |     Single Object            |     Night, mountains, and plains                                |
|     11    |     c           |     1480×684      |     18.5    |     195 seconds    |     258.4 Mb    |     Sunny        |     Multiple Objects         |     Daylight, Night, mountains, and plains                      |
|     12    |     c           |     1480×684      |     21.2    |     190 seconds    |     423.3 Mb    |     Sunny        |     Single Object            |     Daylight, Evening, Night, mountains, and   plains           |
|     13    |     d           |     1480×684      |     9.99    |     133 seconds    |     145.9 Mb    |     Sunny        |     Single Object            |     Daylight, Evening, Night, mountains, lakes,   and plains    |
|     14    |     d           |     1480×684      |     15.7    |     122 seconds    |     169.2 Mb    |     Sunny        |     Multiple Objects         |     Daylight, Evening, Night, mountains, lakes,   and plains    |
|     15    |     d           |     1480×684      |     11.1    |     125 seconds    |     136.5 Mb    |     Sunny        |     No Objects               |     Daylight, Evening, Night, mountains, lakes,   and plains    |
|     16    |     e           |     1280×720      |     30      |     148 seconds    |     348 Mb      |     Sunny        |     Multiple Objects         |     Daylight, mountains, and lakes                              |
|     17    |     e           |     1280×720      |     30      |     97 secnds      |     130.2 Mb    |     Sunny        |     Multiple Objects         |     Night, mountains, and lakes                                 |
|     18    |     e           |     1280×720      |     30      |     89 seconds     |     92 Mb       |     Sunny        |     Multiple Objects         |     Evening, mountains, and lakes                               |
|     19    |     f           |     1280×720      |     24.6    |     60 seconds     |     342.8 Mb    |     Rainy&Fog    |     Multiple Objects         |     Daylight, mountains, lakes, and plains                      |
|     20    |     f           |     1280×720      |     23.7    |     29 seconds     |     20.2 Mb     |     Rainy&Fog    |     Multiple Objects         |      Evening, Night, mountains, lakes, and plains               |
|     21    |     f           |     1280×720      |     10.6    |     57 seconds     |     6.7 Mb      |     Rainy&Fog    |     Multiple Objects         |     Night, mountains, lakes, and plains                         |
|     22    |     f           |     1280×721      |     10.6    |     36 seconds     |     28.1 Mb     |     Rainy&Fog    |     Multiple Objects         |     Evening, mountains, lakes, and plains                       |
|     23    |     g           |     1280×722      |     10.2    |     99 seconds     |     206 Mb      |     Sunny        |     Multiple Objects         |     Daylight, plains                                            |
|     24    |     g           |     1280×723      |     10.5    |     27 seconds     |     21.8 Mb     |     Sunny        |     Multiple Objects         |     Night, plains                                               |
|     25    |     g           |     1280×724      |     9.3     |     61 seconds     |     92 Mb       |     Sunny        |     Multiple Objects         |     Evening, plains                                             |
|     26    |     h           |     1280×724      |     24.7    |     40 seconds     |     251.1 Mb    |     Snow         |     Multiple Objects         |     Daylight, mountains, and plains                             |
|     27    |     h           |     1280×724      |     26      |     33 seconds     |     143.4 Mb    |     Snow         |     Multiple Objects         |     Night, mountains, and plains                                |
|     28    |     h           |     1280×724      |     25.3    |     49 seconds     |     183.6 Mb    |     Snow         |     Multiple Objects         |     Evening, mountains, and plains                              |


## 2.1 多样化场景
我们搭建了八个具有不同地形、不同植被的多种规模森林场景。

![8个不同地形的森林场景，包含平原、山脉、湖泊和河流。](https://user-images.githubusercontent.com/51520993/230010235-ca6fe6c3-9369-4fdc-bfcc-a4be02af4138.png)


## 2.2 多种天气
MSFFD不仅模拟了晴天场景，还模拟了雨雾天和雪天的场景。

![多样化气象条件，包含晴天、雨&雾天和雪天。](https://user-images.githubusercontent.com/51520993/230010663-3901daad-b3ad-4c18-ae02-9f77812deb2b.png)

## 2.3 多个时间
MSFFD考虑了一天中不同时间点（白天，傍晚和黑夜）的多模态森林火灾图像。

![image](https://user-images.githubusercontent.com/51520993/230017256-dd94a59a-7448-499b-a93e-e35d6536b5dd.png)


## 2.4 不同数量的火灾目标
在多种地形、多种气象条件和多个时间点的多模态森林场景下，我们设置了无目标、单个目标和多个目标三种火灾目标数量情况，旨在全面评估模拟多模态森林火灾数据集在目标检测算法的性能表现。

![image](https://user-images.githubusercontent.com/51520993/230016997-8110d8a7-2cc4-4a0f-8f34-b3b1282ee55a.png)


# 3. 数据集的详细信息

下表为数据集的图像和注释框在不同天气和一天中不同时间的分布。


|     Multimodal scenarios    |     Number of images    |     fire    |     smoke    |     Number of annotation boxes    |     Average number of instances boxes per image    |
|-----------------------------|-------------------------|-------------|--------------|-----------------------------------|----------------------------------------------------|
|     Sunny                   |     3292                |     8423    |     7095     |     15518                         |     4.7                                            |
|     Snowy                   |     312                 |     772     |     547      |     1319                          |     4.2                                            |
|     Rainy & Fog             |     370                 |     432     |     494      |     926                           |     2.5                                            |
|     Daytime                 |     2209                |     4684    |     3807     |     8491                          |     3.8                                            |
|     Evening                 |     560                 |     2052    |     1581     |     3633                          |     6.5                                            |
|     Night                   |     1205                |     2891    |     2748     |     5639                          |     4.7                                            |


下表为所有注释框的尺寸分布

|     class    |     small boxes    |     medium boxes    |     large boxes    |     total    |
|--------------|--------------------|---------------------|--------------------|--------------|
|     fire     |     4848           |     4114            |     665            |     9627     |
|     smoke    |     1883           |     2037            |     4216           |     8136     |
|     all      |     6731           |     6151            |     4881           |     17763    |


下图为数据集中注释框的分布情况

![image](https://user-images.githubusercontent.com/51520993/230016724-060d4f17-3e00-4416-a3ca-bf73fa230b58.png)
![image](https://user-images.githubusercontent.com/51520993/230016663-57becf5c-fc60-42d2-b2b0-3dc55af5cf13.png)
![image](https://user-images.githubusercontent.com/51520993/230016547-1f1c81db-013c-4608-9b6e-366c93c157de.png)




# 4. 实验结果

## 4.1 MSFFD在单阶段目标检测算法的实验结果

|     Model         |     #Param.    |     Flops     |     Weight Size    |     AP50:95    |     AP50    |     APFire    |     APSmoke    |     Precision    |     Recall    |     F1-socre    |
|-------------------|----------------|---------------|--------------------|----------------|-------------|---------------|----------------|------------------|---------------|-----------------|
|     YOLOv8m       |     25.9M      |     78.9G     |     52Mb           |     51.2       |     87.3    |     88.7      |     86         |     83.7         |     86.9      |     85.3        |
|     YOLOv8l       |     43.7M      |     165.2G    |     87.7Mb         |     51.6       |     86.8    |     88.9      |     84.8       |     84.6         |     80.1      |     82.3        |
|     YOLOv8x       |     68.2M      |     258.1G    |     136.7Mb        |     47.3       |     87.1    |     88.5      |     85.8       |     84.4         |     80.2      |     82.2        |
|     YOLOv7        |     36.5M      |     103.2G    |     74.8Mb         |     48.5       |     87.5    |     88.7      |     86.2       |     85.3         |     80.5      |     82.8        |
|     YOLOv7-X      |     70.8M      |     188G      |     142.1Mb        |     47.3       |     87.1    |     88.5      |     85.8       |     84.4         |     80.2      |     82.2        |
|     YOLOv6-M      |     34.9M      |     85.8G     |     74.9Mb         |     44.5       |     83.4    |     84.2      |     82.6       |     83.8         |     80.7      |     82.2        |
|     YOLOv6-L      |     59.5M      |     150.7G    |     117.6Mb        |     48.8       |     86.3    |     87.2      |     85.4       |     84.2         |     79.8      |     81.9        |
|     YOLOv6-M6     |     79.6M      |     379.5G    |     72.51Mb        |     43.7       |     82.9    |     82        |     85.1       |     82.6         |     80        |     81.3        |
|     YOLOv6-L6     |     140.4M     |     673.4G    |     268.4Mb        |     46.3       |     83.3    |     83.9      |     82.6       |     83.6         |     79.7      |     81.6        |
|     YOLOv5m       |     21.2M      |     49.0G     |     42.2Mb         |     45.6       |     87.1    |     88.1      |     86         |     86.6         |     81.5      |     84.0        |
|     YOLOv5l       |     46.5M      |     109.1G    |     92.8Mb         |     45.9       |     86.7    |     87.9      |     85.4       |     85.2         |     81.6      |     83.4        |
|     YOLOv5x       |     86.7M      |     205.7G    |     173.1Mb        |     45.7       |     86.3    |     87.3      |     85.3       |     84.6         |     82.3      |     83.4        |
|     YOLOv4        |     -          |     59.6G     |     256Mb          |     -          |     75.3    |     75.7      |     74.8       |     66           |     73        |     69.3        |
|     YOLOv4-CSP    |     -          |     50.3G     |     210.3Mb        |     -          |     81.5    |     83.8      |     79.3       |     78           |     80        |     79.0        |
|     YOLOv3        |     -          |     65.3G     |     246.3Mb        |     -          |     82.3    |     82.6      |     82         |     83           |     77        |     79.9        |
|     YOLOv3-spp    |     -          |     65.7G     |     250.5Mb        |     -          |     82.1    |     82.3      |     81.8       |     83           |     78        |     80.4        |


## 4.2 在双阶段目标检测算法的实验结果

|     Model                    |     Image Size    |     Weight Size    |     AP50:95    |     AP50    |
|------------------------------|-------------------|--------------------|----------------|-------------|
|     Faster R-CNN R50-DC5     |     640           |     1300Mb         |     38.6       |     78.9    |
|     Faster R-CNN R50-FPN     |     640           |     333.3Mb        |     42.1       |     82.7    |
|     Faster R-CNN R50-C4      |     416           |     257.5Mb        |     24.8       |     59.8    |
|     Faster R-CNN R101-C4     |     416           |     422Mb          |     26.9       |     60      |
|     Faster R-CNN R101-DC5    |     416           |     1400Mb         |     25.3       |     57.8    |
|     Faster R-CNN R101-FPN    |     416           |     365.2Mb        |     35.9       |     76.1    |
|     RPN R50                  |     416           |     103.5Mb        |     25.4       |     55.8    |
|     Fast R-CNN  R50-FPN      |     416           |     318.7Mb        |     28.5       |     59.8    |

## 4.3 MSFFD在轻量级目标检测算法的实验结果

|     Model          |     #Param.    |     Flops    |     Weight Size    |     AP50:95    |     AP50    |     APFire    |     APSmoke    |     Precision    |     Recall    |     F1-socre    |
|--------------------|----------------|--------------|--------------------|----------------|-------------|---------------|----------------|------------------|---------------|-----------------|
|     YOLOv8n        |     3.2M       |     8.7G     |     6.3Mb          |     49.5       |     86.4    |     87.1      |     85.7       |     83.2         |     81.2      |     82.2        |
|     YOLOv8s        |     11.2M      |     28.6G    |     22.5Mb         |     50.3       |     86.4    |     87.9      |     85         |     83.1         |     81.4      |     82.2        |
|     YOLOv6-N       |     4.7M       |     11.4G    |     10.0Mb         |     42         |     82.2    |     82.9      |     81.5       |     83.3         |     78.8      |     81.0        |
|     YOLOv6-S       |     18.5M      |     45.3G    |     10.2Mb         |     44.4       |     84.1    |     85        |     83.2       |     83.9         |     80.3      |     82.1        |
|     YOLOv6-N6      |     10.4M      |     49.8G    |     21.83Mb        |     42.1       |     82.1    |     82.8      |     81.3       |     83.7         |     78.9      |     81.2        |
|     YOLOv6-S6      |     41.4M      |     198G     |     85.84Mb        |     43.2       |     83.1    |     83.8      |     82.5       |     83.6         |     79.4      |     81.4        |
|     YOLOv5n        |     1.9M       |     4.5G     |     3.8Mb          |     40.1       |     84.9    |     86.1      |     83.7       |     84.3         |     79.1      |     81.6        |
|     YOLOv5s        |     7.2M       |     16.5G    |     14.4Mb         |     43.7       |     86.4    |     87.9      |     84.9       |     83.7         |     80.9      |     82.3        |
|     YOLOv4-tiny    |     -          |     6.8G     |     23.5Mb         |     -          |     64.5    |     51.9      |     77.1       |     80           |     58        |     67.2        |
|     YOLOv3-tiny    |     -          |     5.4G     |     34.7Mb         |     -          |     71.7    |     69.6      |     73.9       |     76           |     72        |     73.9        |


## 4.4 实验结果可视化

![部分测试图片在不同参数量的算法的检测结果](https://user-images.githubusercontent.com/51520993/230014155-38d8be21-323f-4e1a-a918-f7dc1d2060d1.png)

## 4.5 在真实火灾图像的实验结果

只在真实火灾数据集上训练的实验结果

| Model              |     AP50:95    |     AP50    |     APFire    |     APSmoke    |     Precision    |     Recall    |
|--------------------|----------------|-------------|---------------|----------------|------------------|---------------|
|     YOLOv3-spp     |     27.5       |     54.1    |     63        |     45.2       |     59.9         |     49.2      |
|     YOLOv3         |     27.2       |     53.3    |     62.4      |     44.1       |     59.3         |     49.3      |
|     YOLOv3-tiny    |     21.4       |     42.2    |     53.2      |     31.1       |     70           |     33        |
|     YOLOv5n        |     21.2       |     48.5    |     58.3      |     38.8       |     56           |     47.4      |
|     YOLOv5s        |     23.6       |     50.2    |     60.7      |     39.7       |     57.3         |     50.6      |
|     YOLOv5m        |     24.1       |     52.2    |     61.2      |     43.3       |     57.4         |     49.7      |
|     YOLOv5l        |     24.7       |     53.1    |     62.6      |     43.5       |     56.4         |     52.3      |
|     YOLOv5x        |     25.4       |     53.5    |     62.2      |     44.9       |     58.2         |     51        |
|     YOLOv8n        |     27.6       |     53.5    |     62.3      |     44.6       |     60.1         |     49.3      |
|     YOLOv8s        |     27.1       |     53.5    |     62.3      |     44.6       |     59.7         |     50.3      |
|     YOLOv8m        |     27.2       |     53.7    |     62.6      |     44.8       |     59.2         |     49.5      |
|     YOLOv8l        |     27.7       |     53.8    |     63.4      |     44.1       |     59.2         |     50.7      |
|     YOLOv8x        |     27.7       |     54.1    |     63.1      |     45.1       |     63.3         |     47.6      |


在MSFWD和真实火灾数据集上训练的实验结果

| Model              |     AP50:95    |     AP50    |     APFire    |     APSmoke    |     Precision    |     Recall    |
|--------------------|----------------|-------------|---------------|----------------|------------------|---------------|
|     YOLOv3-spp     |     38         |     69.4    |     71.1      |     67.7       |     72.5         |     63.1      |
|     YOLOv3         |     38.3       |     69.4    |     70.9      |     67.8       |     72.3         |     62.2      |
|     YOLOv3-tiny    |     32.2       |     62.8    |     62.6      |     63.1       |     69.3         |     56.4      |
|     YOLOv5n        |     31.4       |     65.7    |     68.4      |     62.9       |     72.7         |     57.9      |
|     YOLOv5s        |     35.6       |     68.2    |     70.2      |     66.2       |     71.2         |     62.8      |
|     YOLOv5m        |     36         |     69.5    |     71.7      |     67.3       |     72.6         |     62.7      |
|     YOLOv5l        |     36.5       |     69.3    |     71.6      |     67.1       |     71.8         |     63.4      |
|     YOLOv5x        |     37         |     69.9    |     72.1      |     67.7       |     73.6         |     63.4      |
|     YOLOv8n        |     38.3       |     69.3    |     71.6      |     67         |     73.6         |     61.1      |
|     YOLOv8s        |     38.3       |     69.2    |     71        |     67.4       |     72.6         |     62.4      |
|     YOLOv8m        |     39.2       |     70.2    |     71.9      |     68.5       |     73.4         |     63.2      |
|     YOLOv8l        |     39         |     70.6    |     72.5      |     68.7       |     73.7         |     61.9      |
|     YOLOv8x        |     39.2       |     70.3    |     72.2      |     68.5       |     73.4         |     62.4      |


# 5 在Unreal Engine 5中构建数据集
## 5.1 虚幻引擎市场的资源准备

### 5.1.1 注册与登录

- 如果您还没有Epic Games账户：
  - 访问[Epic Games官网](https://www.epicgames.com/store/en-US/)
     ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/2d3516b6-ec30-4d97-b885-96683c14821d)

  - 点击页面右上角的“登陆”，然后选择“注册”。
      ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/58f396a9-8bcf-4aaf-8450-d4ab7ddcd35a)

  - 按照提示填写您的信息并完成验证。

### 5.1.2 浏览与搜索素材

- 打开[虚幻引擎市场](https://www.unrealengine.com/marketplace/en-US/store)。
- 在搜索框中输入关键词，例如：`forest vegetation`、`fire VFX`、`smoke VFX`。  
- 在搜索结果中，您可以按照类别、评分、价格等进行筛选。
   ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/6c62c129-4148-4154-b46e-e1a3fc421c96)


### 5.1.3 素材的选择

- 仔细查看各个产品的：
  - **图片预览**：观察素材的细节、质量以及样式是否符合您的需求。
    ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/91fa785f-bc25-4e91-881f-0811d0107bf3)

  - **视频展示**：如果提供了视频，这可以帮助您更好地了解素材的实际效果。
      ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/501b4837-6441-43c1-b2a0-87040ebdd91c)

  - **用户评价**：其他用户的评价可以为您提供关于该素材的额外信息。
      ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/9a62869a-8290-4d64-ac52-360af2b938be)


### 5.1.4 购买与下载

- 点击您选择的素材。
- 仔细阅读产品描述、技术细节等信息。
- 点击页面右侧的`购买`按钮（如果是付费资源）或`免费领取`（如果是免费资源）。
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/be9907e1-c432-440d-ba22-bb51526b6769)

  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/c76ec82a-9f3b-4485-8517-c45f6e9a49f0)

- 完成购买流程后，该资源将自动添加到您的Epic Games账户库中。
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/6c6c2955-b7c3-4b95-87b0-f8aa345233ba)

- 打开UE5编辑器，进入`Epic Games Launcher`的库，找到你的素材并选择`添加到项目`。
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/57bc90ac-fd11-48c4-b636-09bfafcd66fe)


## 5.2. 场景布局

### 5.2.1 创建新的场景

- 打开UE5编辑器。
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/da1188c7-2f6c-4112-b089-7ccd409ee521)

- 选择`File` > `New Level`，选择一个基本模板，例如“Default”或“VR Basic”。
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/21bb853a-c34b-43e2-8b97-1c26ea8e8158)


### 5.2.2 导入素材

- 打开`Content Browser`，右击，选择`Import`。
  
- 浏览到您从虚幻引擎市场下载的素材目录，选择相关的资源文件进行导入。
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/876a923f-4e62-4213-8dd5-ca280d611629)

### 5.2.3 地形构建：

- 选择左侧工具栏中的“Landscape”工具。
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/62cabe52-fd7b-46cf-8f10-01bef3f40334)


- 在顶部的设置中，调整地形的大小和分辨率，然后点击“创建”。
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/b5a993f7-e043-4fd2-a5ae-baec36e7f672)

- 使用“Sculpt”工具进行雕刻，模仿自然地形的起伏。
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/a74b3727-6687-445c-b09d-11166167847b)



### 5.2.4 植被布局

- 使用`Foliage`工具（通常在主工具栏的左侧）来放置和编辑植被。
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/69ca9ca0-c118-46e8-839e-1a2dd37131d9)

- 在`Foliage`面板中，拖入您要用的植被模型。
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/0222106b-1fcf-4000-bbbc-85c93f6e6fb8)

- 使用画笔工具，调整笔刷大小和强度，在地形上绘制植被。
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/05ef6687-f97d-41c3-8fcd-283d33598f84)


### 5.2.5 火焰和烟雾的放置

- 在`Content Browser`中，找到火焰和烟雾的特效（通常是.particle文件）。
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/eb2cde8e-cdbb-40cc-8006-64c9060845a4)

- 将特效拖入场景中，放在合适的位置。
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/17914bd2-48d9-4913-833f-b76609508c7b)

- 使用`Details`面板来调整特效的大小、方向、强度等属性。
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/5f9a841c-7c7e-4303-bd7e-4b6883b9a348)


### 5.2.6 灯光与相机

- 使用`Place Actors`面板添加灯光，如“Directional Light”、“Point Light”等。
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/6791312f-aead-488d-9995-d927507a5115)

- 调整灯光的位置、方向、颜色和强度来模拟不同的天气和时间条件。
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/0675c4f8-f2e6-4ad7-9ec0-feadba8188ae)

- 添加一个`Camera Actor`到场景中，确定视角和拍摄角度。
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/23b424e8-c820-466d-89d8-83c2cace489f)

- 使用`Details`面板调整相机的焦距、曝光等设置。
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/739dff1b-9259-4985-af4d-e12b5d9c2fec)

### 5.2.7 预览和保存

- 点击`Play`按钮来在编辑器中预览场景。
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/b791d696-78ab-43f1-bff7-3fd2bc817c76)

- 根据需要调整场景的各个元素，直到满意为止。
- 选择`File` > `Save`，为场景命名并保存。
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/0d682560-bba2-4e8d-834a-40ae4f8ca318)



## 5.3 天气、时间和其他细节

### 5.3.1 设置天气

- **晴天**：调整`Directional Light`的强度来模拟阳光，增加`Sky Light`来提供柔和的环境光。
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/394c973e-8bb5-451c-9bcb-74e787577fd0)
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/9cb15535-884d-4613-8d96-d1250f0556c6)
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/87c11903-c36b-4ba3-bd53-3effed820bbd)


- **雨天**：
  - 使用虚幻引擎市场上的雨特效，或者创建自定义的雨滴粒子系统。
  - 调整场景中的所有灯光，使其更暗、更冷。
    ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/3c9bbeb7-b272-4dee-8960-fcb2760ea2ab)

  - 可以考虑增加湿润的地表材质以模拟雨后的地面。
    
- **雾天**：使用`Exponential Height Fog`组件来模拟雾效果。通过调整其属性如雾的密度、颜色和距离，来模拟不同的雾效果。
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/4f78102a-3765-4990-8469-39be4baedde1)


### 5.3.2 调整时间

- **日间**：设置`Directional Light`为明亮的白色，确保天空盒反映出白天的云彩。
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/35d16e00-ec2a-466b-a647-fe97eecd9e66)

- **傍晚**：调整`Directional Light`的颜色为橙红色，降低其强度来模拟日落。
  ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/20dad2ee-d6c5-423b-a2a0-c9d42c2f58df)

- **夜晚**：
  - 设置`Directional Light`的强度非常低，并调整其颜色为深蓝色。
  - 添加`Point Lights`或`Spot Lights`来模拟人工光源，如街灯或灯笼。
  - 考虑增加星空或月亮的天空盒纹理。
    ![image](https://github.com/Philharmy-Wang/M4SFWD/assets/51520993/12ae7329-ce82-47f6-993a-303c4138fd33)


### 5.3.3 其他细节

- **地形**：使用`Landscape`工具来编辑地形，模拟山丘、谷地或平原。使用不同的地表材质来区分地面的不同部分，如泥土、草地或岩石。
- **水体**：为场景添加湖泊或河流，使用虚幻引擎的`Water`系统或第三方插件来模拟水的流动和反射。
- **动态物体**：可以添加一些动态物体来丰富场景，例如飘动的树叶、飞翔的鸟类或其他小动物。


