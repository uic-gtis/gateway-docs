# cameraInfo.csv

## About

The Gateway provides camera snapshot images throughout its coverage area in the form of camera icons on its maps and images in its camera report.

The publicly available `cameraInfo.csv` web service provides [metadata](https://en.wikipedia.org/wiki/Metadata) for the cameras in the Gateway/TravelMidwest.com coverage area with locations and image URLs:

```
https://travelmidwest.com/lmiga/cameraInfo.csv
```

Output is in [comma-separated values (CSV)](https://en.wikipedia.org/wiki/Comma-separated_values) ASCII format suitable for use in spreadsheets (e.g. Microsoft Excel, LibreOffice Calc) and a variety of other applications.

The full output currently includes more than 4,000 camera views:

```csv
ImgPath,CameraLocation,CameraDirection,y,x,SnapShot,WarningAge,TooOld,AgeInMinutes
http://travelmidwest.com/lmiga/showCamera.jsp?id=IL-IDOTD1-IK14B,"Hillside Tower Camera 9",NONE,41.88597,-87.91483,"https://cctv.travelmidwest.com/snapshots/IL-IDOTD1_1_Cook_WB_Albin_4188597_-8791483_2_NONE.jpg",false,false,2
http://travelmidwest.com/lmiga/showCamera.jsp?id=IL-DUPAGECOUNTY-1&direction=E,"County Farm / Main Ent",E,41.8682,-88.144,"https://cctv.travelmidwest.com/snapshots/IL-DUPAGECOUNTY_1_DuPage_NB_County-Farm_4186820_-8814400_1_E.jpg",false,false,1
http://travelmidwest.com/lmiga/showCamera.jsp?id=IL-DUPAGECOUNTY-1&direction=N,"County Farm / Main Ent",N,41.8682,-88.144,"https://cctv.travelmidwest.com/snapshots/IL-DUPAGECOUNTY_1_DuPage_NB_County-Farm_4186820_-8814400_1_N.jpg",false,false,1
http://travelmidwest.com/lmiga/showCamera.jsp?id=IL-DUPAGECOUNTY-1&direction=S,"County Farm / Main Ent",S,41.8682,-88.144,"https://cctv.travelmidwest.com/snapshots/IL-DUPAGECOUNTY_1_DuPage_NB_County-Farm_4186820_-8814400_1_S.jpg",false,false,1
http://travelmidwest.com/lmiga/showCamera.jsp?id=IL-DUPAGECOUNTY-1&direction=W,"County Farm / Main Ent",W,41.8682,-88.144,"https://cctv.travelmidwest.com/snapshots/IL-DUPAGECOUNTY_1_DuPage_NB_County-Farm_4186820_-8814400_1_W.jpg",false,false,1
http://travelmidwest.com/lmiga/showCamera.jsp?id=IL-LAKECOUNTY-659&direction=N,"IL 21 at Casey",N,42.32041,-87.9607,"https://www.lakecountypassage.com/snapshots/IL_21_@_Casey_cctv_North_Leg.jpg",false,false,8
http://travelmidwest.com/lmiga/showCamera.jsp?id=IL-LAKECOUNTY-659&direction=S,"IL 21 at Casey",S,42.32041,-87.9607,"https://www.lakecountypassage.com/snapshots/IL_21_@_Casey_cctv_South_Leg.jpg",false,false,8
http://travelmidwest.com/lmiga/showCamera.jsp?id=IL-LAKECOUNTY-659&direction=W,"IL 21 at Casey",W,42.32041,-87.9607,"https://www.lakecountypassage.com/snapshots/IL_21_@_Casey_cctv_West_Leg.jpg",false,false,8
http://travelmidwest.com/lmiga/showCamera.jsp?id=IL-IDOTD1-IK23,"Nordic",NONE,41.95833,-88.02554,"https://cctv.travelmidwest.com/snapshots/IL-IDOTD1_1_DuPage_WB_I-290_4195833_-8802554_1_NONE.jpg",false,false,1
```

The first line is a header row providing field/column labels for the remaining rows:

| Column | Value |
| --- | --- |
| ImgPath | **Warning:**<br>The **ImgPath** column is still included for legacy and compatibility reasons but its public use has been deprecated and no longer supported after December 13, 2024. Please use the URLs provided in the **SnapShot** column instead.<br>Links to a snapshot display with the option to select from different camera views if available:<br>![camera_pop-up.366x370.jpg](images/camera_pop-up.366x370.jpg) |
| CameraLocation | Text description of where the camera is located. |
| CameraDirection | This is the direction a multi-directional camera was facing when it took its snapshot picture. Uni-directional cameras will always have "NONE" in this field. The valid values for this field are N, NE, NW, S, SE, SW, E, W, and NONE.<br>The following diagram depicts a uni-directional camera that faces only east. It is represented in `cameraInfo.csv` as one row of data with the camera's latitude, longitude, and the URL of the one image file it provides.<br>![Unidirectional Camera Diagram](images/unidirectional-camera-diagram.svg)<br>Multi-directional cameras pan, tilt, and zoom as part of automated programs so that they can see more than one direction of traffic. These cameras pan, tilt, and zoom to face one direction, snap a picture, move to the next direction, snap a picture, etc. These cameras have one latitude and longitude coordinate but provide multiple images.<br>The following diagram depicts a multi-directional camera that faces east and west as part of its automated routine. When it faces east it creates the `image_east.jpg` file and when it faces west it creates the `image_west.jpg` file.<br>![Multidirection Camera Diagram](images/multidirection-camera-diagram.svg) |
| y | Latitude in decimal degrees using the WGS84 datum. |
| x | Longitude in decimal degrees using the WGS84 datum. |
| SnapShot |  |

Public download URL for a camera's image file suitable for custom applications. Additional details are available in our [XML and Camera Image Download Manual](user-guides-and-manuals/xml-and-camera-image-download-manual.md#camera-images).
|  |  |
| --- | --- |
| WarningAge | If no image has been received from the camera for 10 minutes, then this field will be "true", otherwise it will be "false".If no image has been received from the camera for 30 minutes, then this field will be "true", otherwise it will be "false". |
| TooOld | If no image has been received from the camera for 30 minutes, then this field will be "true", otherwise it will be "false". |
| AgeInMinutes | This is the number of minutes that have elapsed between the time the `cameraInfo.csv` file was downloaded and when the camera last sent an image to the Gateway/TravelMidwest.com. |

## ArcGIS Online Integration

ArcGIS Online provides an "Add Layer from Web" function that can be used along with `cameraInfo.csv` to provide a camera layer for use on web sites.

It creates a point feature using the coordinates. The pop-up can be edited to use the ‘Snapshot’ attribute to show the image~:

![ArcGIS_Online.Add_Layer_from_Web.2018-7-18_7-29-52.560x300.jpg](images/ArcGIS_Online.Add_Layer_from_Web.2018-7-18_7-29-52.560x300.jpg)![ArcGIS_Online.point_feature.2018-7-18_7-28-26.593x300.jpg](images/ArcGIS_Online.point_feature.2018-7-18_7-28-26.593x300.jpg)

Questions and/or comments can be addressed to: [webmaster@travelmidwest.com](mailto:webmaster@travelmidwest.com?subject=cameraInfo.csv)
