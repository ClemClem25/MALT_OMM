# Installation Guide for MALT at the "Centre de Primatologie de Strasbourg"

This project is mainly for the installation of each MALT at the "Centre de Primatologie de Strasbourg".

You will find resources to install the package OMM with some modified codes from the original version that you can find here: [OMM GitHub Repository](https://github.com/open-cogsci/omm-client).

Here is the list of the main modifications:

- **OMM Conditioner: JuicePumpCdp**  
  A new conditioner that allows you to send a "start character", a "stop character", and a "duration" in seconds, which defines the time between each sending of the character. You also have the checkbox "Juice".  
  Example of usage: Our pump with its interface card works this way: you need to send `px` (where `x` is a number between 0 and 9 or `m`) to define the power of the pump (`m` being maximal). To turn it off, send `p0`.

- **OMM Detect Participant**  
  You can read two serial ports "at the same time", which is very useful at the "Centre de Primatologie de Strasbourg" as we have 2 RFID detectors. Furthermore, the code has been modified to enable detection on 15 bytes with a separator, a `;`, between each RFID.

## How to install or update on a new mini-PC:

1) **Install OpenSesame**: [Download OpenSesame](https://osdoc.cogsci.nl/4.0/download/#windows)  
2) **Install the OMM library**:  
   `pip install https://github.com/open-cogsci/omm-client/archive/refs/tags/prerelease/0.7.0a3.zip`  
   Here is the link where each release is downloaded: [OMM Releases](https://github.com/open-cogsci/omm-client/releases/tag/prerelease%2F0.7.0a3)  
3) **Modify each folder/file from this repository**  
   Replace the contents of the folder `OpenSesame\Lib\site-packages\opensesame_plugins\open_monkey_mind` with the new ones from this GitHub (folder `Install_folder_V1`).
4) **Switch the COM ports for the RFID readers and the pump to the following**:  
   This step is necessary because each test is coded with these COM ports as references.  
   - Pump = Port COM24  
   - RFID Reader = Port COM23  
   - RFID Reader = Port COM22  
5) **In OpenSesame**, go to "Tools > Preferences" and scroll down until you find "Entry point (for connecting to the server)".  
   Click on it after you have verified that the server is correctly configured and connected. Then you need to do 2 things:
   1. Change the wait image to an image of a banana, which you can download from the "Set_of_Essentials" folder in this GitHub.
   2. Change the serial ports for the "detect" condition.
