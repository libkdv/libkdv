# LIBKDV - A Versatile Kernel Density Visualization Library for Geospatial Analytics

# Background:
Kernel Density Visualization (KDV) has been extensively used for many geospatial analysis tasks. Some representative examples include traffic accident hotspot detection, crime hotspot detection, and disease outbreak detection. Although many scientific software packages, including Scipy and Scikit-learn, geographical software packages, including QGIS and ArcGIS, and visualization software packages, including Deck.gl and KDV-Explorer, can also support KDV, none of these tools, to the best of our knowledge, can be scalable to high resolution size (e.g., 2560 x 1920) and large-scale datasets (e.g., one million data points). Therefore, the huge computational cost limits the applicability of using the off-the-shelf software tools to support advanced (or more complex) geospatial analytics, e.g., bandwidth-tuning analysis and spatiotemporal analysis, which involves computing multiple KDVs in one batch.

# Description of LIBKDV:
To overcome the above issue, we develop the first versatile programming library (LIBKDV) that can reduce the worst-case time complexity for supporting different types of KDV-based geospatial analytics (based on our recent studies, SLAM [1] and SWS [2]), including:

(1)	Bandwidth-tuning analysis: Domain experts can first set multiple bandwidths in a batch, and then generate multiple KDVs with respect to these bandwidths.

(2)	Spatiotemporal analysis: Domain experts can leverage a more complex spatiotemporal kernel density function to generate time-dependent hotspot maps that correspond to different timestamps.

To further enhance the efficiency for these two tasks, we fully parallelize our methods, SLAM and SWS.

<!-- <img width="849" alt="03e58de5950a5d503b73952e8a3bbd1" src="https://user-images.githubusercontent.com/96175669/146165826-eef5f116-3e37-4bec-91dc-899af61fed18.png">-->

# How to use

# Core source codes


# Project members
[Dr. (Edison) Tsz Nam Chan](https://www.comp.hkbu.edu.hk/~edisonchan/), Hong Kong Baptist University<br />
[Mr. Pak Lon Ip], Universiy of Macau<br />
[Mr. Kaiyan Zhao], Universiy of Macau<br />
[Prof. Ryan L.H. U](https://www.fst.um.edu.mo/personal/ryanlhu/), Universiy of Macau<br />
[Dr. Byron Choi](https://www.comp.hkbu.edu.hk/~bchoi/), Hong Kong Baptist University<br />
[Prof. Jianliang Xu](https://www.comp.hkbu.edu.hk/~xujl/), Hong Kong Baptist University<br />

# Publications
[1] Tsz Nam Chan, Leong Hou U, Byron Choi, Jianliang Xu. SLAM: Efficient Sweep Line Algorithms for Kernel Density Visualization. Proceedings of ACM Conference on Management of Data (SIGMOD), 2022.

[2] Tsz Nam Chan, Pak Lon Ip, Leong Hou U, Byron Choi, Jianliang Xu. SWS: A Complexity-Optimized Solution for Spatial-Temporal Kernel Density Visualization. Proceedings of the VLDB Endowment (PVLDB), 2022.
