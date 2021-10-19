# IEEE 2030.5 네트워크 프로토콜을 이용한 실시간 분산 에너지 자원 시스템 시뮬레이터

## ※ 2021 IEEE ISGT-Asia 발표 예정



## Abstract

IEEE 2030.5 standard is drawing special attention among communication protocols for smart inverters and distributed energy resources (DER). Moreover, California Rule 21 mandates new DER must be ready to communicate to a host utility using the IEEE 2030.5 standard. Therefore, development of an effective real-time simulation method for managing DER using IEEE 2030.5 network is crucial. This paper presents a real-time hardware-in-the-loop (HIL) DER system testbed using the IEEE 2030.5 standard. The proposed real-time co-simulation testbed consists of a DER physical system simulation using OPAL-RT real-time simulator and a cyber system simulation including DER gateways and a DER management system (DERMS) cloud server. Custom-built client and server programs are developed to meet the compliant with IEEE 2030.5-2018 standard and implemented in the DER gateways and a DERMS server, respectively. The feasibility of the proposed testbed for DER systems is validated by experiments.


## IEEE 2030.5 protocol

IEEE 2030.5 standard defines an application protocol which provides an interface between the smart grid and users via internet and enables to manage the end user energy environment such as demand response, load control, price communication.

IEEE 2030.5 was previously named the SEP and based on Zigbee Alliance as a metering communication solution for building energy devices. In 2013, SEP2 was originally developed after adopted and ratified by IEEE (i.e., IEEE 2030.5-2013). In 2016, CPUC chose this protocol as the default protocol for Rule 21. The revision, IEEE 2030.5-2018, provides an expanded feature set that supports all controls in IEEE 1547-2018.


### Communication hierarchy in testbed
![communication](https://user-images.githubusercontent.com/88572107/136975957-fd81d82d-e3c4-4a32-a486-984ca7fd19b6.PNG)


## Testbed structure

![structure](https://user-images.githubusercontent.com/88572107/136767866-10c6db9c-9457-4429-b6e2-257c09f34f43.png)

## Distributed Energy Resource

<img width="525" alt="Screen Shot 2021-10-14 at 11 37 05 PM" src="https://user-images.githubusercontent.com/88572107/137339582-03409680-eb43-4978-bb1c-5418ed92fa75.png">

Figure above illustrates a DER system in IEEE 13 Node Test Feeder circuit where the DER system consists of multiple smart inverters, a swing bus, a wind turbine (WT), a Photovoltaic (PV), an energy storage system (ESS) and loads. The system bus frequency is 60Hz and the nominal voltage is 4.16kV. Smart inverters of WT and PV perform maximum power point tracking (MPPT) control. The WT of the 634 bus is applied with the permanent magnet synchronous generator (PMSG) model and the rated power is 2.2 MVA. The PV is located on bus 675 and the rated output is 1MW. The ESS capacity of bus 680 is 1 MWh and a lithium-ion battery model is used. Except for the bus where the generators are connected, the resistive, inductive, and capacitive loads are evenly connected to the other buses, where the real power demand of the distribution system is 3.5 MW; the reactive power demand of inductive loads is 2.102 MVAR; and the reactive power demand of capacitive loads is 0.7 MVAR. The impedance values between the buses are chosen based on the IEEE 13 bus system. The DERM system model is implemented in MATLAB/Simulink. 



#### A DER system in IEEE 13 node test feeder circuit, monitored and controlled by a DERMS.

## Experiment setup

![그림1](https://user-images.githubusercontent.com/88572107/136767642-f89d0e36-ef7c-4940-b5bd-88fe5a106b75.png)

## Cloud based DERMS web page

<img width="672" alt="Screen Shot 2021-07-14 at 3 04 03 AM" src="https://user-images.githubusercontent.com/88572107/137153104-f471fd73-78dc-4fea-a65f-4fdf1f4e1a3f.png">


Figure above shows the custom-built DERMS cloud server web page. DERMS server is implemented on a virtual private server. The server runs on Ubuntu 18.04 and uses Apache2 HTTP server project to host the server. Python 3.6.9 and Django REST Framework are used to meet the technical components of IEEE 2030.5-2018 standard as mentioned insection II. In server, real-time DER system data such as reactive power or power factor are stored in local SQLite3 database. Such data are linked with identification data like sfdi (Short-form device identifier). These data are visualized in server as a graph in real time using Python library named pyplot from matplotlib.


## Validation

### Encrypted traffic with TLS 1.3 captured by WireShark

![wireshark](https://user-images.githubusercontent.com/88572107/137153324-4e37f9be-f4df-4cab-ad39-8cca0fe715c2.png)


DER Gateways (i.e., IP: 165.246.223.92) and DERMS cloud server (i.e., IP: 69.164.199.161) are connected. Figure shows that the screenshot of the encrypted exchanging data between them by TLS 1.3 in WireShark. We can see all the data is encrypted and just showed as Application Data. Also, it is expected that TLS v1.3 provides fast processing time than TLS v1.2 since the number of round trips has been reduced in TLS v1.3.
