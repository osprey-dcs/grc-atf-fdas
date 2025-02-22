# NASA GRC-ATF FDAS D.4.1 - Functional Checkout

Analysis (A) - the verification of a product or system using models, calculations and testing equipment.

Inspection (I) - the non-destructive examination of a product or system using one or more of the five senses.

Demonstration (D) - the manipulation of the product or system as it is intended to be used to verify that the results are as planned or expected.

Test (T) - the verification of a product or system using a controlled and predefined series of inputs, data, or stimuli to ensure that the product or system will produce a very specific and predefined output as specified by the requirements.

## F.1 System Facility Interface Requirements
The NASA GRC-ATF SEC FDAS shall be designed to conform to the following overall system design requirements:
<table border="1" style="border-collapse: collapse; width: 100%;">
    <tr>
        <th>ID</th>
        <th>Requirement</th>
        <th>Value</th>
        <th>Verify</th>
    </tr>
    <tr>
        <td>F.1.1</td>
        <td>Electrical Power</td>
        <td>Single Phase 120 VAC</td>
        <td>I</td>
    </tr>
    <tr>
        <td>F.1.2</td>
        <td>Operating Temperature</td>
        <td>0° C to 40° C</td>
        <td>A</td>
    <tr>
    <tr>
        <td>F.1.3</td>
        <td>Operating Humidity</td>
        <td>Less than 90%</td>
        <td>I</td>
    </tr>
    <tr>
        <td rowspan="3">F.1.4</td>
        <td rowspan="3">External UTC Time Source</td>
        <td>The following:</td>
        <td><a href="D-3-1_DESIGN_-_Design_and_Architecture.md#372---irig-timeserver">D</a> </td>
    </tr>
        <tr>
            <td>IRIG-B</td>
            <td>D</td>
        <tr>
            <td>GPS</td>
            <td>D</td>
        </tr>
    <tr>
        <td>F.1.5</td>
        <td>Form Factor</td>
        <td>Standard 19" wide rack mount</td>
        <td>I</td>
    </tr>
    <tr>
        <td>F.1.6</td>
        <td>Max Width</td>
        <td>≤ 3 standard racks (total)</td>
        <td>I</td>
    </tr>
        <tr>
        <td>F.1.7</td>
        <td>Max Height</td>
        <td>≤ 44U rack height (each)</td>
        <td>I</td>
    </tr>
    <tr>
        <td rowspan="4">F.1.8</td>
        <td rowspan="4">Analog Input Connector</td>
        <td>All analog input connection shall conform to the following:</td>
        <td></td>
    </tr>
        <tr>
            <td>37 DB (MILD STD tbd)</td>
            <td>I</td>
        <tr>
            <td>16 differential voltage input channels per 37 DB</td>
            <td>I</td>
        </tr>
        <tr>
            <td>Pin-out per NASA SPEC (tbd)</td>
            <td>I</td>
        </tr>
    <tr>
        <td>F.1.9</td>
        <td>System Component Distributability</td>
        <td>All data processing components shall be able to be distributed via standard Ethernet (IEEE-802.x)</td>
        <td>I</td>
    </tr>
</table>

## F.2 Digitizing Electronics
The NASA GRC-ATF SEC FDAS Digitizing Electronics shall be design to digitize analog signals in accordance with the following Digitizing Electronics requirements:
<table border="1" style="border-collapse: collapse; width: 100%;">
    <tr>
        <th>ID</th>
        <th>Requirement</th>
        <th>Value</th>
        <th>Verify</th>
    </tr>
    <tr>
        <td>F.2.1</td>
        <td>Number of Channels</td>
        <td>≥ 1,024 Channels</td>
        <td><a href="D-3-1_DESIGN_-_Design_and_Architecture.md#42411---functional-description-of-the-daq-ioc">I</a></td>
    </tr>
    <tr>
        <td rowspan="6">F.2.2</td>
        <td rowspan="6">Data Sample Rates</td>
        <td>Including, but not limited to:</td>
        <td><a href="D-4-10_PROC_-_Quartz_QA.md#test-at-all-frequencies">T</a></td>
    </tr>
        <tr>
            <td>1. 250 kSPS @ 256 CH</td>
            <td>D, T</td>
        <tr>
            <td>2. 50 kSPS @ 1,024 CH</td>
            <td>D, T</td>
        </tr>
        <tr>
            <td>3. 25 kSPS @ 1,024 CH</td>
            <td>D, T</td>
        </tr>
        <tr>
            <td>4. 5 kSPS @ 1,024 CH</td>
            <td>D, T</td>
        </tr>
        <tr>
            <td>5. 1 kSPS @ 1,024 CH</td>
            <td>D, T</td>
        </tr>
    <tr>
        <td>F.2.3</td>
        <td>Data Sample Rate Selectability</td>
        <td>User selectable from the DAS software application</td>
        <td><a href="D-4-5_PROC_-_Making_a_Recording_Procedure.md#preparation">D</a></td>
    <tr>
    <tr>
        <td>F.2.4</td>
        <td>Input Type</td>
        <td>Direct Voltage Input, Pre-conditioned signals</td>
        <td>I</td>
    <tr>
    <tr>
        <td>F.2.5</td>
        <td>Channel Input Range</td>
        <td>± 10 V</td>
        <td>D, <a href="D-4-10_PROC_-_Quartz_QA.md#signal-check-all-dc">T</a></td>
    </tr>
    <tr>
        <td>F.2.6</td>
        <td>ADC Resolution</td>
        <td>≥ 24-bit</td>
        <td>I, <a href="D-4-10_PROC_-_Quartz_QA.md#signal-check-all-dc">T</a></td>
    </tr>
    <tr>
        <td>F.2.7</td>
        <td>Channel-to-Channel Synchronization</td>
        <td>± 0.1 μs</td>
        <td>T</td>
    </tr>
    <tr>
        <td>F.2.8</td>
        <td>Crosstalk Rejection</td>
        <td>≥ 80 dB DC to 2 kHz</td>
        <td><a href="D-4-10_PROC_-_Quartz_QA.md#crosstalk-check">T</a></td>
    </tr>
    <tr>
        <td>F.2.9</td>
        <td>AC/DC Input Coupling</td>
        <td>Per-channel selectable</td>
        <td><a href="D-4-10_PROC_-_Quartz_QA.md#toggle-channels-to-dc">T</a></td>
    </tr>
    <tr>
        <td>F.2.10</td>
        <td>AC/DC Input</td>
        <td>User selectable from the DAS software application</td>
        <td><a href="D-4-5_PROC_-_Making_a_Recording_Procedure.md">D</td>
    </tr>
    <tr>
        <td>F.2.11</td>
        <td>Input Impedance</td>
        <td>≥ 100 kΩ</td>
        <td>I</td>
    </tr>
    <tr>
        <td>F.2.12</td>
        <td>Gain Accuracy</td>
        <td>≥ ± 0.5% DC</td>
        <td><a href="D-4-10_PROC_-_Quartz_QA.md#toggle-channels-to-dc">T</a></td>
    </tr>
    <tr>
        <td rowspan="7">F.2.13</td>
        <td rowspan="7">Measurement Bandwidth</td>
        <td>Alias free measurements from DC to:</td>
        <td><a href="D-4-10_PROC_-_Quartz_QA.md#test-at-all-frequencies">T</a></td>
    </tr>
    <tr>
        <tr>
            <td>1. 100 kHz @ 250 kSPS</td>
            <td>T</td>
        <tr>
            <td>2. 20 kHz @ 50 kSPS</td>
            <td>T</td>
        </tr>
        <tr>
            <td>3. 10 kHz @ 25 kSPS</td>
            <td>T</td>
        </tr>
        <tr>
            <td>4. 2 kHz @ 5 kSPS</td>
            <td>T</td>
        </tr>
        <tr>
            <td>5. 400 Hz @ 1 kSPS</td>
            <td>T</td>
        </tr>
    </tr>
    <tr>
        <td>F.2.14</td>
        <td>Passband Ripple</td>
        <td>≤ 0.1 dB</td>
        <td>T</td>
    </tr>
    <tr>
        <td>F.2.15</td>
        <td>Digitizer On-board FMC</td>
        <td>Yes, user programmable</td>
        <td>I</td>
    </tr>
    <tr>
        <td>F.2.16</td>
        <td>Digitizer On-board FMC Firmware Source Code Availability</td>
        <td>Open-sourcable, BSD or similar</td>
        <td><a href="D-1-4_BOM_-_List_of_Software_and_Firmware.csv">I</a></td>
    </tr>
    <tr>
        <td>F.2.17</td>
        <td>Digitizer On-board FMC Firmware Source Code Licensing</td>
        <td>Open-sourcable, BSD or similar</td>
        <td><a href="D-1-4_BOM_-_List_of_Software_and_Firmware.csv">I</a></td>
    </tr>
    <tr>
        <td>F.2.18</td>
        <td>Digitizer Timing System Interface</td>
        <td>Event-based, 100% mRF* protocol compatible</td>
        <td><a href="D-1-4_BOM_-_List_of_Software_and_Firmware.csv">I</a></td>
    </tr>
    <tr>
        <td>F.2.19</td>
        <td>Digitizer DAS Application Interface</td>
        <td>100% Open-Standards-based</td>
        <td><a href="D-1-4_BOM_-_List_of_Software_and_Firmware.csv">I</a></td>
    </tr>
    <tr>
        <td>F.2.20</td>
        <td>Digitizer DAS Application Interface Driver Licensing</td>
        <td>Open-Sourcable, BSD or similar</td>
        <td><a href="D-1-4_BOM_-_List_of_Software_and_Firmware.csv">I</a></td>
    </tr>
</table>

\* The mRF timing spec is published at http://mrf.fi/fw/DCManual-191127.pdf

## F.3 Data Recording
<table border="1" style="border-collapse: collapse; width: 100%;">
    <tr><th>ID</th><th>Requirement</th><th>Value</th><th>Verify</th></tr>
    <tr><td>F.3.1</td><td>Storage Reliability</td><td>≥ RAID 5</td><td>I</td></tr>
    <tr><td>F.3.2</td><td>1,024 Channel Individual Recording Duration</td><td>≥ 15 minutes for full 1,024 channels all acquiring at 50 kHz Sample Rate</td><td>T</td></tr>
    <tr><td>F.3.3</td><td>256 Channel Individual Recording Duration</td><td>≥ 15 minutes for partial 256 channels acquiring at 250 kHz Sample Rate</td><td>T</td></tr>
    <tr><td>F.3.4</td><td>Number of Consecutive Recordings Prior to System Offload</td><td>≥ 15 recordings each case</td><td>A</td></tr>
    <tr><td>F.3.5</td><td>Recording Timestamping vs UTC</td><td>± 0.1 μs</td><td>T</td></tr>
    <tr><td rowspan="7">F.3.6</td><td rowspan="7">Per Recording Meta-Data Capture</td><td>The following (at a min)</td><td></td></tr>
        <tr><td>1. Customer Name</td><td>D</td></tr>
        <tr><td>2. Project ID</td><td>D</td></tr>
        <tr><td>3. Test Facility</td><td>D</td></tr>
        <tr><td>4. Recording ID</td><td>D</td></tr>
        <tr><td>5. Recording Start Time</td><td>D</td></tr>
        <tr><td>6. Operator Name</td><td>D</td></tr>
    <tr><td rowspan="12">F.3.7</td><td rowspan="12">Per Channel Calibration Data Capture</td><td>The following (at a min)</td><td></td></tr>
        <tr><td>1. Channel ID</td><td>D</td>
        <tr><td>2. Digitizer ID</td><td>D</td></tr>
        <tr><td>3. Cal. Slope</td><td>D</td></tr>
        <tr><td>4. Cal. Offset</td><td>D</td></tr>
        <tr><td>5. EU Slope</td><td>D</td></tr>
        <tr><td>6. EU Offset</td><td>D</td></tr>
        <tr><td>7. EU Unit</td><td>D</td></tr>
        <tr><td>8. Calibration Date</td><td>D</td></tr>
        <tr><td>9. DMM Make</td><td>D</td></tr>
        <tr><td>10. DMM Model</td><td>D</td></tr>
        <tr><td>11. DMM SN</td><td>D</td></tr>
   <tr><td rowspan="3">F.3.8</td><td rowspan="3">Calibration Settings</td><td>The following (at a min)</td><td></td></tr>
        <tr><td>1. Calibration Scope</td><td>I, D</td></tr></tr>
        <tr><td>2. Calibration Offset</td><td>I, D</td></tr>
   <tr><td rowspan="3">F.3.9</td><td rowspan="3">EU Conversion Configuration</td><td>The following (at a min)</td><td></td></tr>
        <tr><td>1. EU conversion slope</td><td>I, D</td></tr>
        <tr><td>2. EU conversion offset</td><td>I, D</td></tr>
</table>

[D.4.5 - Making a Recording](D-4-5_PROC_-_Making_a_Recording_Procedure.md)

## F.4 Real-Time Monitoring (RTM)
The SEC-FDAS shall be capable of monitoring channel data in real-time in a manner that fulfills the following minimum real-time monitoring requirements:

<table border="1" style="border-collapse: collapse; width: 100%;">
    <tr><th>ID</th><th>Requirement</th><th>Value</th><th>Verify</th></tr>
    <tr><td>F.4.1</td><td>Channel Availability for RTM</td><td>All</td><td>D</td></tr>
    <tr><td>F.4.2</td><td>Number of RTM PCs</td><td>≥ 2</td><td>I, D</td></tr>
    <tr><td>F.4.3</td><td>Simultaneous RTM channels</td><td>≥ 16 per RTM PC</td><td>D</td></tr>
    <tr><td>F.4.4</td><td>RTM FFT Analysis Option</td><td>All channels fully selectable</td><td>D</td></tr>
    <tr><td>F.4.5</td><td>RTM Power Spectral Density (PSD) Analysis Option</td><td>All channels as selected</td><td>D</td></tr>
    <tr><td>F.4.6</td><td>RTM Time Domain Analysis Option</td><td>All channels as selected</td><td>D</td></tr>
    <tr><td>F.4.7</td><td>RTM Peak Detection Feature</td><td>All channels as selected</td><td>D</td></tr>	
    <tr><td>F.4.8</td><td>RTM Display Measurement to Display Latency</td><td>≤ 0.5 seconds</td><td>T</td></tr>
</table>

[D.4.6 - Monitoring a Data Channel in Real Time](D-4-6_PROC_-_Monitoring_a_Data-Channel_in_Real_Time.md)

## F.5 Software Application
The NASA GRC-ATF SEC FDAS Software Application shall be designed to meet or exceed the following minimum system software application requirements:

<table border="1" style="border-collapse: collapse; width: 100%;">
    <tr><th>ID</th><th>Requirement</th><th>Verify</th></tr>
    <tr><td>F.5.1</td><td>Software Architecture conforms to the Neil A. Armstrong Test Facility Common DAC System System Architecture Specification revision 72260 dated August 14, 2023</td><td>A</td></tr>
    <tr><td>F.5.2</td><td>GUI interface for all specified functions</td><td>I</td></tr>
    <tr><td>F.5.3</td><td>Alarm and Limit Summary Display and Monitoring capability</td><td><a href="D-3-1_DESIGN_-_Design_and_Architecture.md#437---alarm-management-functionality">D</a></td></tr>
    <tr><td>F.5.4</td><td>Whole system configuration Save and Restore capability</td><td><a href="D-3-1_DESIGN_-_Design_and_Architecture.md#439---system-save-and-restore-functionality">T</a></td></tr>
    <tr><td rowspan="2">F.5.5</td><td>The DAS system will be able to define all User-defined Per-Test channel configuration using a CSV Import capability where the CSV has the following columns:</td><td rowspan="2"><a href="D-4-4_PROC_-_Per_Test_User_Configuration_Procedure.md">D</a></td></tr>
    <tr>
        <td class="split-cell">
            <div><table>
                <tr><th>Column Name</th><th></th><th>Description</th></tr>
                <tr><td>SIGNAL</td><td>=</td><td>Overall System CH #</td></tr>
                <tr><td>CHASSIS</td><td>=</td><td>Digitizer #</td></tr>
                <tr><td>CHANNEL</td><td>=</td><td>Digitizer Channel #</td></tr>
                <tr><td>CONNECTOR</td><td>=</td><td>Digitizer Connector #</td></tr>
                <tr><td>USE</td><td>=</td><td>Channel Use (Yes/No)</td></tr>
                <tr><td>CUSTNAM</td><td>=</td><td>Channel User Label</td></tr>
                <tr><td>DESC</td><td>=</td><td>Channel Description</td></tr>
                <tr><td>IDLINE5</td><td>=</td><td>UFF58 meta-data</td></tr>
                <tr><td>RESPNODE</td><td>=</td><td>UFF58 meta-data</td></tr>
                <tr><td>RESPDIR</td><td>=</td><td>Response Direction</td></tr>
                <tr><td>SPECDATATYP</td><td>=</td><td>Specific Data Type field</td></tr>
                <tr><td>EGU</td><td>=</td><td>engineering unit</td></tr>      
            </table></div>
            <div><table>
                <tr><th>Column Name</th><th></th><th>Description</th></tr>
                <tr><td>CUSTMEASLOC</td><td>=</td><td>Custom Measurement Location</th></tr>
                <tr><td>ESLO</td><td>=</td><td>Volts to EU Slope</th></tr>
                <tr><td>EOFF</td><td>=</td><td>Volts to EU Offset</th></tr>
                <tr><td>MAXEULVL</td><td>=</td><td>Max EU level (before clip)</th></tr>
                <tr><td>SAMPLPERSEC</td><td>=</td><td>Sample Rate</th></tr>
                <tr><td>HIlim</td><td>=</td><td>High Warning Level (in EU)</th></tr>
                <tr><td>LOlim</td><td>=</td><td>Low Warning Level (in EU)</th></tr>
                <tr><td>HIHIlim</td><td>=</td><td>High Alarm Limit (in EU)</th></tr>
                <tr><td>LOLOlim</td><td>=</td><td>Low Alarm Limit (in EU)</th></tr>
                <tr><td>COUPLING</td><td>=</td><td>Coupling (AC or DC)</th></tr>
                <tr><td>CONFIGTIMEID</td><td>=</td><td>Configuration Timestamp</th></tr>
                <tr><td>DBREL</td><td>=</td><td>EU value for dB relative calculations</th></tr>
            </table></div>
        </td>
    </tr>
    <tr><td rowspan="2">F.5.6</td><td>Current User-defined Per-Test channel configuration CSV export capability</td><td>T</td>
    <tr><td>CSV export (fields same as import)</td><td><a href="D-4-8_PROC_-_Export_Data_from_the_System.md">I</a></td></tr>
    <tr><td>F.5.7</td><td>Electronic Logbook capability</td><td><a href="D-3-1_DESIGN_-_Design_and_Architecture.md#4310---electronic-logbook---epics-olog-service-and-client">D</a></td></tr>	
    <tr><td rowspan="3">F.5.8</td><td>General/Universal Screenshot capability</td><td>D</td>
    <tr><td>automatic filenaming with timestamps</td><td>D</td></tr>
    <tr><td>automatic filename included in the screenshot</td><td>D</td></tr>
</table>

## F.6 Configuration by CSV
The NASA GRC-ATF SEC FDAS shall be able to import a single CSV file that configures the per-test channel configurations with the following features:

<table border="1" style="border-collapse: collapse; width: 100%;">
    <tr><th>ID</th><th>Requirement</th><th>Value</th><th>Verify</th></tr>
    <tr><td>F.6.1</td><td>The DAC system shall be able to support per-test user-defined channel channel labels of the following length:</td><td>≥ 40 characters</td><td>D</td></tr>
    <tr>
        <td rowspan = "10">F.6.2</td>
        <td rowspan = "10">The DAC system shall be able to utilize the following characters as valid characters in the per-test user-defined channel channel labels:</td>
    </tr>
    <tr><td>Uppercase letters ( A-Z )</td><td>D</td></tr>
    <tr><td>Lowercase  letters ( a-z )</td><td>D</td></tr>
    <tr><td>Numbers ( 0-9 )</td><td>D</td></tr>
    <tr><td>Parentheses " ( " and " ) "</td><td>D</td></tr>
    <tr><td>Minus sign ( - )</td><td>D</td></tr>
    <tr><td>Plus Sign ( + )</td><td>D</td></tr>
    <tr><td>Asterisk ( * )</td><td>D</td></tr>
    <tr><td>Periods ( . )</td><td>D</td></tr>
    <tr><td>Underscores ( _ )</td><td>D</td></tr>
</table>

[D.4.4 - User Configuration Procedure](D-4-4_PROC_-_Per_Test_User_Configuration_Procedure.md)

## F.7 Data Export
The NASA GRC-ATF SEC FDAS shall be designed to export recorded data in accordance with the following data export requirements:

<table border="1" style="border-collapse: collapse; width: 100%;">
    <tr><th>ID</th><th>Requirement</th><th>Verify</th></tr>
    <tr><td>F.7.1</td><td>from user selectable recordings</td><td>D</td></tr>
    <tr><td>F.7.2</td><td>from user selectable channels</td><td>D</td></tr>
    <tr><td>F.7.3</td><td>from user selectable time ranges</td><td>D</td></tr>
    <tr><td>F.7.4</td><td>in user selectable formats</td><td>D</td></tr>
    <tr><td>F.7.5</td><td>in the CSV format</td><td>D</td></tr>
    <tr><td>F.7.6</td><td>in the UFF58b format</td><td>D</td></tr>
</table>

[D.4.8 - Data Export Procedure](D-4-8_PROC_-_Export_Data_from_the_System.md)

## F.8 UFF58 Export Header Requirements
The NASA GRC-ATF SEC FDAS shall be designed to export UFF58 recorded data in accordance with the following UFF58 data export format requirements:

<table border="1" style="border-collapse: collapse; width: 100%;">
    <tr><th>ID</th><th>Requirement</th><th>Verify</th></tr>
       <tr><td rowspan="2">F.8.1</td><td>Exported UFF58 files shall contains the following numeric values in the Response Direction field (Field 7) based on the Response Direction column data in the input configuration CSV as follows:</td><td rowspan="2">T</td></tr>
    <tr>
        <td class="split-cell">
            <div><table>
                <tr><th>CSV String</th><th></th><th>Field 7 Value</th></tr>
                <tr><td>blank</td><td>=</td><td>0</td></tr>
                <tr><td>X+</td><td>=</td><td>1</td></tr>
                <tr><td>Y+</td><td>=</td><td>2</td></tr>
                <tr><td>Z+</td><td>=</td><td>3</td></tr>
                <tr><td>XR+</td><td>=</td><td>4</td></tr>
                <tr><td>YR+</td><td>=</td><td>5</td></tr>
                <tr><td>ZR+</td><td>=</td><td>6</td></tr>
            </table></div>
            <div><table>
                <tr><th>CSV String</th><th></th><th>Field 7 Value</th></tr>
                <tr><td>scalar</td><td>=</td><td>0</td></tr>
                <tr><td>X-</td><td>=</td><td>-1</td></tr>
                <tr><td>Y-</td><td>=</td><td>-2</td></tr>
                <tr><td>Z-</td><td>=</td><td>-3</td></tr>
                <tr><td>XR-</td><td>=</td><td>-4</td></tr>
                <tr><td>YR-</td><td>=</td><td>-5</td></tr>
                <tr><td>ZR-</td><td>=</td><td>-6</td></tr>
            </table></div>
        </td>
    </tr>
    <tr>
        <td rowspan="2">F.8.2</td>
        <td>Exported UFF58b files shall contains the following numeric values in the Specific Data Type field (Field 1) based on the Specific Data Type column data in the input configuration CSV as follows:</td>
        <td rowspan="2">T</td>
    </tr>
    <tr>
        <td class="split-cell">
            <div><table>
                <tr><th>CSV String</th><th></th><th>Field 4 Value
                <tr><td>blank</td><td>=</td<td>0</td></tr>
                <tr><td>unknown</td><td>=</td<td>0</td></tr>
                <tr><td>general</td><td>=</td><td>1</td></tr>
                <tr><td>stress</td><td>=</td><td>2</td></tr>
                <tr><td>strain</td><td>=</td><td>3</td></tr>
                <tr><td colspan="2"4 is skipped</td></tr>
                <tr><td>temperature</td><td>=</td><td>5</td></tr>
                <tr><td>heat flux</td><td>=</td><td>6</td></tr>
            </table></div>
            <div><table>       
                <tr><th>CSV String</th><th></th><th>Field 4 Value
                <tr><td colspan="2"7 is skipped</td></tr>
                <tr><td>displacement</td><td>=</td><td>8</td></tr>
                <tr><td>reaction force</td><td>=</td><td>9</td></tr>
                <tr><td colspan="2"10 is skipped</td></tr>
                <tr><td>velocity</td><td>=</td><td>11</td></tr>
                <tr><td>acceleration</td><td>=</td><td>12</td></tr>
                <tr><td>excitation force</td><td>=</td><td>13</td></tr>
                <tr><td colspan="2"14 is skipped</td></tr>
            </table></div>  
            <div><table>              
                <tr><th>CSV String</th><th></th><th>Field 7 Value
                <tr><td>pressure</td><td>=</td><td>15</td></tr>
                <tr><td>sound pressure</td><td>=</td><td>15</td></tr>
                <tr><td>mass</td><td>=</td><td>16</td></tr>
                <tr><td>time</td><td>=</td><td>17</td></tr>
                <tr><td>frequency</td><td>=</td><td>18</td></tr>
                <tr><td>rpm</td><td>=</td><td>19</td></tr>
                <tr><td>order</td><td>=</td><td>20</td></tr>
            </table></div>        
        </td>
    </tr>
</table>

[D.4.8 - Data Export Procedure](D-4-8_PROC_-_Export_Data_from_the_System.md)

## F.9 Secure Web-Based Data Export
<table border="1" style="border-collapse: collapse; width: 100%;">
    <tr><th>ID</th><th>Requirement</th><th>Verify</th></tr>
    <tr>
        <td rowspan="2">F.9.1</td><td><b>The DAC system shall include a local open-source web-server that facilitates secure data export by making a specific folder (and any subfolders) accessible to remote network clients from a standard web-browser.</b></td>
        <td  rowspan="2">D</td>
        </tr>
        <tr><td><i>Rationale - The DAC operator needs to be able to provide the data to the Facility's Data Export System without the need for removable media.</i></td></tr>
    <tr>
        <td rowspan="2">F.9.2</td><td><b>The DAC system export web server will not expose any files or folders on the system that contain any OS system or DAC application processes or configuration data.</b></td>
        <td  rowspan="2">D</td>
        </tr>
        <tr><td><i>Rationale - Remote clients should only be able to access data the the DAC operator has staged in a special location for export as required by NASA's' Zero-Trust Architecture rules for Data at Rest (DAR)</i></td></tr>
    <tr>
        <td rowspan="2">F.9.3</td><td><b>The DAC system's web server shall run using a self-signed certificate that enables the remote browser-based client to obtain data from the system using the https protocol on port 443.</b></td>
        <td  rowspan="2">D</td>
        </tr>
        <tr><td><i>Rationale - The DAC systems web-server must be capable of conforming to NASA's Zero-Trust Architecture rules for Data In Transit (DIT). The use of a self-signed cert forces the provider to configure the webserver for cert use. NASA will provide the final trusted cert separately.</i></td></tr>
    <tr>
        <td>F.9.4</td><td><b>The DAC system's data export webserver shall be capable of switching from a self-signed certificate to a NASA provided certificate without changing the webserver configuration. The DAC operator will be able to simply replace the self-signed cert with the NASA cert and restart the webserver service.</b></td>
        <td>D</td>
        </tr>

[D.4.8 - Data Export Procedure](D-4-8_PROC_-_Export_Data_from_the_System.md)
