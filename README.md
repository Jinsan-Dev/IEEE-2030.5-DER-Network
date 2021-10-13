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

## Experiment setup

![그림1](https://user-images.githubusercontent.com/88572107/136767642-f89d0e36-ef7c-4940-b5bd-88fe5a106b75.png)

## Cloud based DERMS web page

<img width="672" alt="Screen Shot 2021-07-14 at 3 04 03 AM" src="https://user-images.githubusercontent.com/88572107/137153104-f471fd73-78dc-4fea-a65f-4fdf1f4e1a3f.png">

Here we can see data from OPAL-RT

## Validation



