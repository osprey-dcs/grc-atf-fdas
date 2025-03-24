# NASA GRC-ATF FDAS D.4.10 - Quartz Quality Assurance
## Purpose
The purpose of this document is to have a consistent unified way each Quartz Board is tested before deployment. This procedure will be updated periodically to improve QA of the boards.

## Equipment needed
* Stanford Research Systems DS360 Low Distortion Generator
* 2 x BNC to DB37 Cable (BNC to All channels)
* BNCs to DB37 Cable (BNC to Individual Channel)
* Multimeter (Fluke 115 or better)
* Triple output Benchtop Power Supply 
* 2 x FMC Power breakout module [link](https://www.iamelectronic.com/shop/produkt/fpga-mezzanine-card-fmc-power-module/)
* Marble Testing Chassis
* PC to run IOC and Phoebus

## Procedure
### Visual Inspection
Check visual for any board defects. If the board has come back from rework look at the reworked areas carefully under magnification for any shorts etc.

Areas to check with extra scrutiny are around the ADC chips, around the Relays, the clocking distribution components.

<div align="center"><b>Record in Testing Log when complete</b></div>
<p></p>

***

### Power Testing
Next the Board will be powered up in various ways to protect other testing hardware.

***

### Looking for Shorts to GND
Using the multimeter check that all voltage
[test points](https://github.com/osprey-dcs/Quartz/blob/quartz-1.x/Documentation/Quartz%20Test%20Points.pdf)
have a resistance to board ground greater than 1kΩ.

| Test Point Reference | SilkscreenedLabel | Nominal Voltage |
| ---- | ---- | ---- |
| TP 1 | P1_2P5V | +2.5V  |
| TP 2 | P2_2P5V | +2.5V  |
| TP 3 | +5V | +5V  |
| TP 4 | +3.3V | +3.3V  |
| TP 5 | +16V | +16V  |
| TP 6 | +15V | +15V  |
| TP 7 | -15V | -15V  |
| TP 8 | -16V | -16V  |
| TP 9 | GND | 0V  |
| TP 10 | GND | 0V  |
| TP 11 | +12V | +12V  |

<div align="center"><b>Record in Testing Log when complete</b></div>
<p></p>

***

### 12V/3.3V/2.5V Power Testing
One at a time inject 12V,3.3V & 2.5V using the voltage test points found on the board. Do this with a 1.5A current limit.

Note variance from nominal current if found.

Nominal expected current draw is:
<table border="1"; style="border-collapse: collapse;">
    <tbody>
        <tr><td>12V</td><td>~850mA</td></tr>
        <tr><td>3.3V</td><td>&lt;100mA</td></tr>
        <tr><td>2.5V</td><td>&lt;100mA</td></tr>
    </tbody>
</table>

<div align="center"><b>Record in Testing Log when complete</b></div>
<p></p>

***

### FMC breakout Power Testing
Using a 3 output power supply and two FMC Power breakout modules: Power up all input power rails (12V/3.3V/2.5V) simultaneously

Note variance from nominal current if found.

Nominal expected current draw is:
<table border="1"; style="border-collapse: collapse;">
    <tbody>
        <tr><td>12V</td><td>~850mA</td></tr>
        <tr><td>3.3V</td><td>&lt;100mA</td></tr>
        <tr><td>2.5V</td><td>&lt;100mA</td></tr>
    </tbody>
</table>

<div align="center"><b>Record in Testing Log when complete</b></div>
<p></p>

***

### Power up with Marble
Attach a now power tested quartz to a **powered off** marble testing chassis.

Power up the testing chassis.

Start the IOC.

Ensure proper readback of diagnostic quartz signal (voltage, etc.).

<div align="center"><b>Record in Testing Log when complete</b></div>
<p></p>

***

### Signal Check All DC
Until mentioned otherwise, connect the DS360 Low Distortion Generator output (with output disabled) to a tee then to two BNC to DB37 Cables (BNC to All channels). Connect the two DB37 ends to the Quartz Inputs.
* Set Data Acquisition to 250kHz sampling in Phoebus
* Set all Channels to DC input coupling
* Run the following signals into all channels simultaneously
* +/-10V amplitude sine wave at 10kHz
* +/-9V with a +0.5V DC offset amplitude sine wave at 10kHz
* 0V

Look at real-time min/max/average/std. deviation results of all channels while injecting these signals and look for any outliers or anomalous readings or high noise.

<div align="center"><b>Record in Testing Log when complete</b>

*note this covers NASA GRC-ATF F.2.5 Testing  
*note this covers NASA GRC-ATF F.2.6 Testing
</div>

***

### Signal Check All AC
* Set Data Acquisition to 250kHz sampling in Phoebus
* Set all Channels to AC input coupling
* Run the following signals into all channels simultaneously
    * +/-10V amplitude sine wave at 10kHz
    * +/-9V with a +0.5V DC offset amplitude sine wave at 10kHz
    * 0V

Look at real-time min/max/average/std. deviation results of all channels while injecting these signals and look for any outliers or anomalous readings.

<div align="center"><b>Record in Testing Log when complete</b></div>

***

### Toggle Channels to DC
* Set Data Acquisition to 250kHz sampling in Phoebus
* Set all Channels to **AC input coupling**; should already be their if following along
* Run the following signal into all channels simultaneously
    * +/-9V with a +0.5V DC offset amplitude sine wave at 10kHz
* Toggle each channel to DC mode one at a time and observe the 0.5V offset appearing in the real time readback data.

<div align="center"><b>Record in Testing Log when complete</b>

*note this covers NASA GRC-ATF F.2.9 Testing  
*note this covers NASA GRC-ATF F.2.12 Testing; looking at DC reading in average
</div>

***

### Toggle Channels to AC
* Set Data Acquisition to 250kHz sampling in Phoebus
* Set all Channels to DC input coupling
* Run the following signal into all channels simultaneously
    * +/-9V with a +0.5V DC offset amplitude sine wave at 10kHz
* Toggle each channel to AC mode one at a time and observe the 0.5V offset disappearing in the real time readback data.

<div align="center"><b>Record in Testing Log when complete</b></div>

***

### Test at All frequencies
* Set all Channels to **DC input coupling**
* Run the following signal into all channels simultaneously
    * +/-9V with a +0.5V DC offset amplitude; log sine wave sweep from 100Hz to 100kHz @ 0.2Hz rate
* Set Data Acquisition to 250kHz sampling in Phoebus
* Look at FFT of channels for anomalous results
##
* Set Data Acquisition to 50kHz sampling in Phoebus
* Change sweep to 100Hz to 25kHz @ 0.2Hz rate
* Look at FFT of channels for anomalous results
##
* Set Data Acquisition to 25kHz sampling in Phoebus
* Change sweep to 100Hz to 13kHz @ 0.2Hz rate
* Look at FFT of channels for anomalous results
##
* Set Data Acquisition to 5kHz sampling in Phoebus
* Change sweep to 50Hz to 3kHz @ 0.2Hz rate
* Look at FFT of channels for anomalous results
##
* Set Data Acquisition to 1kHz sampling in Phoebus
* Change sweep to 10Hz to 500Hz @ 0.2Hz rate
* Look at FFT of channels for anomalous results
##

<div align="center"><b>Record in Testing Log when complete</b>

*note this covers NASA GRC-ATF F.2.2 Testing
*note this covers NASA GRC-ATF F.2.13 Testing
</div>

***

### Crosstalk Check
* Disable the DS360 Low Distortion Generator output.
* Replace testing cables with the BNCs to DB37 Cable (BNC to Individual Channel)
* Inject a +/-10V amplitude; log sine wave sweep from 100Hz to 100kHz @ 0.2Hz rate in 4 random channels one at a time (1 random channel on each of the board’s ADC)
* Look to see that other channels are below ~56e-6 times lower than the channel with signal.
    * Note any channels above the expected nominal 15e-6 times (~ -95dB) level 

<div align="center"><b>Record in Testing Log when complete</b>

*note this covers NASA GRC-ATF F.2.8 Testing
</div>

***

### EEPROM Programmed

According to the [Quartz EEPROM](https://github.com/osprey-dcs/quartz-daq-250-24/blob/master/documentation/chassis-setup.md#quartz-eeprom) programming guide,
checkout the branch/revision appropriate to the PCB model to be programmed,
and edit `createEEPROMs.sh` with the appropriate serial numbers.

For the Quartz version 1 PCBs delivered, use the `quartz-1.x` branch.

<div align="center"><b>Record in Testing Log when complete</b></div>

## Start/Completion Validation

<br/>

Performed By: ______________________

<br/>

Date Initiated: ______________________

<br/>

Date Completed: ______________________

<br/>

- [ ] Check to indicate that this procedure was performed with no deviations or waivers

<br/>

QA Verification by: ______________________

<br/>

QA Verification Date: ______________________
