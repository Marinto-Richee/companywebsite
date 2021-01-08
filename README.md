# Web Design for a Manufacturing Company
## AIM: 
To design a static website for a chip manufacturing company.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Updating the sample content.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 6:
Publish the website in the given URL.

## PROGRAM:

### splbase.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Silicon Private Limited</title>
    <link rel="stylesheet" href="{% static 'css/siliconprivatelimited.css' %}">
    <link rel="icon" href="{% static 'images/letter-m.png' %}" type="image/x-icon">
</head>
 
<body>

    <div class="parallax">
        <h1 id="title">Silicon<br>Private<br>Limited</h1>
    </div>
    <div class="sticky">
        <nav><a href="http://marinto.student.saveetha.in:8000/splhome/" style="color: #FAB162"> Home</a>
            <a href="http://marinto.student.saveetha.in:8000/splproducts/" style="color: #FAB162">Products</a>
            <a href="http://marinto.student.saveetha.in:8000/splpeople/" style="color: #FAB162">People</a>
            <a class='space' href="http://marinto.student.saveetha.in:8000/splcontact/" style="color: #FAB162">Contact
                Us</a>
        </nav>
    </div>
    <div>
        {% block content %}
        {% endblock  %}
        <footer>Copyright &COPY; 2020 Silicon Private Limited, Developed by Marinto Richee J.</footer>
    </div>
</body>

</html>
```

### splhome.html
```
{% extends "website/splbase.html" %}
{% block content %}

<h2>About Us</h2>
<img class="imgstyle" src="/static/images/spl.gif" alt="company">
<p>Silicon Pvt Ltd, provides a wide range of semiconductor and infrastructure software applications that serve
    the data center, networking, software, broadband, wireless, and storage and industrial markets. Common
    applications for its products include data center networking, home connectivity, broadband access,
    telecommunucations equipment, smartphones, base stations, data center servers and storage, factory
    automation, power generation and alternative energy systems, displays,and mainframe operations and
    management, and application software development. Some of Silicon's core technologies and products include:
</p>
<ul class="margin">
    <li>Memory Chips</li>
    <li>SATA HDD</li>
    <li>SATA SSD</li>
    <li>Broadband Modems</li>
    <li>Wifi Devices</li>
    <li>Switching Devices</li>
    <li>Optical Sensors</li>
</ul>
{% endblock  %}
```
### splproducts.html
```
{% extends "website/splbase.html" %}
{% block content %}
<div>
    <h1>Our Premium Products</h1>
    <div class="product">
        <h2>RAM</h2>
        <img class="imgstyle1" src="/static/images/ram1.jpg" alt="p1">
        <h3>HyperX Fury 8GB 3200MHz DDR4 CL16 DIMM 1Rx8 Black XMP Desktop Memory</h3>
        <h4>Price:3300<br><a href="https://www.amazon.in/dp/B07WJJ9CNG/ref=cm_sw_em_r_mt_dp_JxR9FbP70Y4EK"
                target="_blank"><img class="logo" src="/static/images/amazon.jpeg" alt="a1"></a></h4>

        <img class="imgstyle1" src="/static/images/ram2.jpg" alt="p2">
        <h3>XPG ADATA GAMMIX D30 DDR4 8GB (1x8GB) 3200MHz U-DIMM Desktop Memory</h3>
        <h4>Price:3450<br><a href="https://www.amazon.in/dp/B085HSGQ1Y/ref=cm_sw_em_r_mt_dp_3BR9FbSRGA59G"
                target="_blank"><img class="logo" src="/static/images/amazon.jpeg" alt="a2"></a></h4>
    </div>
    <div class="product">
        <h2>SATA HDD</h2>
        <img class="imgstyle1" src="/static/images/hdd1.jpg" alt="p3">
        <h3>Seagate BarraCuda 1 TB Internal Hard Drive HDD – 3.5 Inch SATA 6 Gb/s 7200 RPM 64 MB Cache for Computer
            Desktop PC</h3>
        <h4>Price:3400<br><a href="https://www.amazon.in/dp/B01LNJBA2I/ref=cm_sw_r_cp_apa_i_xLR9Fb6B03FRF"
                target="_blank"><img class="logo" src="/static/images/amazon.jpeg" alt="a3"></a></h4>
        <img class="imgstyle1" src="/static/images/hdd2.jpg" alt="p4">
        <h3>Western Digital WD Blue WD20EZAZ 2TB 5400 RPM 256MB Cache SATA 6.0Gb/s 3.5" Latest Internal Hard Drive </h3>
        <h4>Price:4999<br><a href="https://www.amazon.in/dp/B07M7Q3FXG/ref=cm_sw_r_cp_apa_i_HMR9FbGPR4XAR"
                target="_blank"><img class="logo" src="/static/images/amazon.jpeg" alt="a4"></a></h4>

    </div>
    <div class="product">
        <h2>SATA SSD</h2>
        <img class="imgstyle1" src="/static/images/ssd1.jpg" alt="p5">
        <h3>Western Digital WD Green 240 GB 2.5 inch SATA III Internal Solid State Drive</h3>
        <h4>Price:2530<br><a href="https://www.amazon.in/dp/B076Y374ZH/ref=cm_sw_r_cp_apa_i_FNR9FbMCCZDVY"
                target="_blank"><img class="logo" src="/static/images/amazon.jpeg" alt="a5"></a></h4>

        <img class="imgstyle1" src="/static/images/ssd2.jpg" alt="p6">
        <h3>Crucial BX500 240GB 3D NAND SATA 2.5-inch SSD</h3>
        <h4>Price:2410<br><a href="https://www.amazon.in/dp/B07G3YNLJB/ref=cm_sw_r_cp_apa_i_iOR9Fb6V2GMPH"
                target="_blank"><img class="logo" src="/static/images/amazon.jpeg" alt="a6"></a></h4>

    </div>
    <div class="product">
        <h2>Broadband Modems</h2>
        <img class="imgstyle1" src="/static/images/modem1.jpg" alt="p7">
        <h3>TP-LINK TD-W8961N Wireless N300 ADSL2+ Wi-Fi Modem Router, 2x 5dBi Omni directional Fixed antennas,Input
            ISPs supported- BSNL, MTNL, Tata Indicom (RJ-11 Port)</h3>
        <h4>Price:1280<br><a href="https://www.amazon.in/dp/B00RK5VU5M/ref=cm_sw_r_cp_apa_i_BPR9Fb38TQ6EP"
                target="_blank"><img class="logo" src="/static/images/amazon.jpeg" alt="a7"></a></h4>
        <img class="imgstyle1" src="/static/images/modem2.jpg" alt="p8">
        <h3>TP-Link Archer C50 AC1200 Dual Band Wireless Cable Router, Wi-Fi Speed Up to 867 Mbps/5 GHz + 300 Mbps/2.4
            GHz, Supports Parental Control, Guest Wi-Fi, VPN</h3>
        <h4>Price:1999<br><a href="https://www.amazon.in/dp/B071RSD473/ref=cm_sw_r_cp_apa_i_5PR9FbKR2HZYE"
                target="_blank"><img class="logo" src="/static/images/amazon.jpeg" alt="a8"></a></h4>

    </div>
    <div class="product">
        <h2>Wifi Devices</h2>
        <img class="imgstyle1" src="/static/images/wifi1.jpg" alt="p9">
        <h3>Tenda N301 Wireless-N300 Easy Setup Router</h3>
        <h4>Price:1540<br><a
                href="https://www.amazon.in/dp/B00D3GO8R4/ref=cm_sw_r_cp_apa_i_YQR9FbXNVWXPP?_encoding=UTF8&psc=1"
                target="_blank"><img class="logo" src="/static/images/amazon.jpeg" alt="a9"></a></h4>

        <img class="imgstyle1" src="/static/images/wifi2.jpg" alt="p10">
        <h3>TP-Link USB WiFi Adapter for PC(TL-WN725N), N150 Wireless Network Adapter for Desktop - Nano Size WiFi
            Dongle Compatible with Windows 10/7/8/8.1/XP/ Mac OS 10.9-10.15 Linux Kernel 2.6.18-4.4.3</h3>
        <h4>Price:499<br><a href="https://www.amazon.in/dp/B008IFXQFU/ref=cm_sw_r_cp_apa_i_eSR9Fb05DTZ71"
                target="_blank"><img class="logo" src="/static/images/amazon.jpeg" alt="a10"></a></h4>

    </div>
    <div class="product">
        <h2>Switching Devices</h2>
        <img class="imgstyle1" src="/static/images/switchingdevices1.jpg" alt="p11">
        <h3>XORB WiFi Socket Switch Plug for Smart Devices</h3>
        <h4>Price:899<br><a href="https://www.amazon.in/dp/B07G16P31F/ref=cm_sw_r_cp_apa_i_5SR9FbTGYE0J4"
                target="_blank"><img class="logo" src="/static/images/amazon.jpeg" alt="a11"></a></h4>

        <img class="imgstyle1" src="/static/images/switchingdevices2.jpg" alt="p12">
        <h3>wipro Wi-Fi Enabled Smart LED Bulb B22 9-Watt (16 Million Colors + Warm White/Neutral
            White/White)(Compatible with Amazon Alexa and Google Assistant)</h3>
        <h4>Price:1499<br><a href="https://www.amazon.in/dp/B08C83HKJS/ref=cm_sw_r_cp_apa_i_HTR9FbNRCD005"
                target="_blank"><img class="logo" src="/static/images/amazon.jpeg" alt="a12"></a></h4>

    </div>
</div>
{% endblock  %}
```
### splpeople.html
```
{% extends "website/splbase.html" %}
{% block content %}

<div>
    <img class="imgstyle2" src="/static/images/administration.png" alt="CEO">
    <h2 class="designation">CEO</h2>
    <h3>Mr.Chris Evans</h3>


</div>
<div>
    <img class="imgstyle2" src="/static/images/business.jpeg" alt="DBI">
    <h2 class="designation">Director of Business Intelligence</h2>
    <h3>Mr.Robert Downey Junior</h3>
</div>
<div>
    <img class="imgstyle2" src="/static/images/economics.jpeg" alt="DED">
    <h2 class="designation">Director of Economic Developement</h2>
    <h3>Mr.Mark Ruffalo</h3>


</div>
<div>
    <img class="imgstyle2" src="/static/images/engineering.jpg" alt="DES">
    <h2 class="designation">Director of Engineering sector</h2>
    <h3>Mrs.Elizabeth Olsen</h3>

</div>
<div>

    <img class="imgstyle2" src="/static/images/security1.jpg" alt="DSS">
    <h2 class="designation">Director of Safety and Security</h2>
    <h3>Mr.Chris Hemsworth</h3>
</div>
<div>

    <img class="imgstyle2" src="/static/images/sales11.jpg" alt="DS">
    <h2 class="designation">Director of Sales </h2>
    <h3>Mrs.Brie Larson</h3>

</div>
{% endblock  %}
```
### splcontactus.html
```
{% extends "website/splbase.html" %}
{% block content %}
<div>
    <img class="imgstyle1" src="/static/images/customer.jpeg" alt="contact">
    <h1>Contact
    </h1>
    <h3>Email: siliconprivate@yahoo.com</h3>
    <h3>Phone: 999-888-77-66</h3>
    <br>
    <br>
    <br>
</div>
{% endblock  %}
```

## OUTPUT:
![output](./static/images/outputhome.jpg)

![output](./static/images/outputproduct.jpg)

![output](./static/images/outputpeople.jpg)

![output](./static/images/outputcontactus.jpg)

## CODE VALIDATION REPORT:
![output](./static/images/vhome.jpg)
![output](./static/images/vproduct.jpg)
![output](./static/images/vpeople.jpg)
![output](./static/images/vcontact.jpg)


## RESULT:
Thus a website is designed for the chip manufacturing company and is hosted in the URL http://marinto.student.saveetha.in:8000/splhome/. HTML code is validated.