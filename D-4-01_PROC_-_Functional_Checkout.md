# FDAS System Functional Checkout

The purpose of this procedure is to bring the FDAS system
into a known functional state.

## 1. Prerequisites

- Availability of a CCCR file configuring the channels to be verified to a voltage scale.  (no EGU, ESLO=1.0, ESLO=0.0)
- Locate function generator (eg. Agilent 33220 Waveform generator)
- Locate test cable set as described in [D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md).

## 2. Preparation

Configuring function generator for AC response test

1. Function generator
  1. Reset function generator to defaults
    - May exclude settings known not to effect output, eg. network address
    - May use setting save/restore feature
  1. Ensure output is disabled
  1. Set output to high impedance (HighZ)
  1. Select sine wave
  1. Set offset to zero volts
  1. Set amplitude +-5 V (10 Vpp)
  1. Set frequency to 9 KHz

Note: Running [D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)
      will reconfigure the function generator.
      It is recommended to reset and setup, then save settings once,
      and thereafter restore settings following each calibration run.

## 3. Expected Response

Figure 1. Chassis Scope screen showing expected response to 9 KHz sine wave.

![Expected response](image/quartz-250ksps-9khz-sine-20Vpp-full.png)

Figure 2. Chassis Scope zoomed in in both time and frequency.

![Expected response](image/quartz-250ksps-9khz-sine-20Vpp-zoom.png)

Essential frequency (FFT) response characteristics.

- Primary peak at 9 KHz
    - Amplitude of 5 V
    - Sharp peak <= 3 frequency points
- No other peaks above -80 dB relative (0.0005 V)

The important relationship is the relative size of the peak at 9 KHz to all other peaks,
which should be at least -80 dB less ($10^\frac{-80}{20} = \frac{1}{10000} = 0.0001$).

By default, the
[Chassis Scope](D-4-06_PROC_-_Monitoring_a_Data-Channel_in_Real_Time.md)
screen shows FFT on a log/log plot with base 10.

To simplify interpretation, adjust the FFT Plot scale so that
only peaks above the -80 dB threshold will be visible.
Leave the horizontal scale on auto.

- Change vertical scale to 1e-6 -> 10
- Uncheck auto-scale

Right click on the plot area and select `Configure Plot` from the menu which appears.

Figure 3. Phoebus plot configuration dialog

![Plot config](image/Phoebus_plot_config.png)

## 4. Process

1. Run through the "System Power Down" section of [D.4.3](D-4-03_PROC_-_Start-up_and_Shut-down.md).
1. Run through the "System Power Up" section of [D.4.3](D-4-03_PROC_-_Start-up_and_Shut-down.md).
1. Run [D.4.9](D-4-09_PROC_-_Inspecting_the_Current_State_and_Health.md.) Inspecting the Current State and Health of the system
1. Set sample rate to 50Ksps and enable acquisition.  (see [D.4.6](D-4-06_PROC_-_Monitoring_a_Data-Channel_in_Real_Time.md))
1. Chassis 1.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-01.csv`](cccr/D-4-01-chassis-01.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 1.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 2.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 3.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 4.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 5.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 6.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 7.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 8.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 9.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 10.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 11.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 12.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 13.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 14.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 15.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 16.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 17.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 18.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 19.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 20.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 21.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 22.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 23.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 24.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 25.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 26.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 27.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 28.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 29.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 30.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 31.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 32.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 2.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-02.csv`](cccr/D-4-01-chassis-02.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 33.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 34.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 35.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 36.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 37.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 38.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 39.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 40.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 41.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 42.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 43.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 44.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 45.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 46.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 47.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 48.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 49.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 50.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 51.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 52.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 53.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 54.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 55.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 56.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 57.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 58.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 59.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 60.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 61.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 62.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 63.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 64.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 3.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-03.csv`](cccr/D-4-01-chassis-03.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 65.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 66.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 67.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 68.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 69.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 70.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 71.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 72.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 73.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 74.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 75.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 76.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 77.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 78.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 79.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 80.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 81.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 82.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 83.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 84.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 85.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 86.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 87.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 88.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 89.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 90.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 91.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 92.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 93.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 94.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 95.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 96.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 4.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-04.csv`](cccr/D-4-01-chassis-04.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 97.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 98.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 99.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 100.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 101.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 102.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 103.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 104.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 105.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 106.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 107.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 108.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 109.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 110.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 111.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 112.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 113.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 114.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 115.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 116.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 117.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 118.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 119.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 120.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 121.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 122.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 123.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 124.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 125.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 126.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 127.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 128.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 5.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-05.csv`](cccr/D-4-01-chassis-05.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 129.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 130.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 131.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 132.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 133.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 134.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 135.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 136.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 137.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 138.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 139.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 140.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 141.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 142.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 143.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 144.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 145.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 146.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 147.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 148.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 149.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 150.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 151.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 152.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 153.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 154.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 155.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 156.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 157.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 158.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 159.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 160.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 6.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-06.csv`](cccr/D-4-01-chassis-06.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 161.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 162.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 163.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 164.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 165.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 166.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 167.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 168.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 169.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 170.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 171.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 172.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 173.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 174.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 175.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 176.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 177.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 178.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 179.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 180.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 181.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 182.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 183.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 184.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 185.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 186.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 187.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 188.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 189.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 190.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 191.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 192.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 7.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-07.csv`](cccr/D-4-01-chassis-07.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 193.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 194.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 195.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 196.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 197.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 198.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 199.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 200.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 201.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 202.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 203.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 204.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 205.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 206.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 207.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 208.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 209.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 210.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 211.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 212.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 213.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 214.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 215.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 216.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 217.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 218.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 219.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 220.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 221.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 222.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 223.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 224.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 8.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-08.csv`](cccr/D-4-01-chassis-08.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 225.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 226.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 227.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 228.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 229.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 230.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 231.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 232.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 233.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 234.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 235.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 236.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 237.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 238.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 239.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 240.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 241.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 242.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 243.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 244.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 245.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 246.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 247.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 248.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 249.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 250.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 251.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 252.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 253.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 254.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 255.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 256.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 9.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-09.csv`](cccr/D-4-01-chassis-09.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 257.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 258.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 259.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 260.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 261.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 262.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 263.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 264.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 265.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 266.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 267.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 268.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 269.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 270.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 271.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 272.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 273.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 274.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 275.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 276.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 277.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 278.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 279.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 280.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 281.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 282.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 283.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 284.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 285.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 286.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 287.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 288.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 10.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-10.csv`](cccr/D-4-01-chassis-10.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 289.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 290.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 291.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 292.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 293.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 294.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 295.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 296.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 297.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 298.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 299.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 300.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 301.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 302.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 303.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 304.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 305.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 306.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 307.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 308.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 309.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 310.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 311.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 312.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 313.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 314.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 315.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 316.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 317.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 318.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 319.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 320.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 11.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-11.csv`](cccr/D-4-01-chassis-11.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 321.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 322.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 323.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 324.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 325.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 326.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 327.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 328.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 329.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 330.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 331.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 332.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 333.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 334.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 335.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 336.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 337.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 338.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 339.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 340.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 341.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 342.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 343.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 344.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 345.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 346.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 347.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 348.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 349.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 350.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 351.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 352.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 12.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-12.csv`](cccr/D-4-01-chassis-12.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 353.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 354.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 355.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 356.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 357.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 358.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 359.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 360.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 361.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 362.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 363.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 364.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 365.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 366.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 367.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 368.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 369.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 370.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 371.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 372.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 373.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 374.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 375.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 376.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 377.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 378.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 379.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 380.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 381.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 382.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 383.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 384.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 13.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-13.csv`](cccr/D-4-01-chassis-13.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 385.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 386.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 387.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 388.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 389.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 390.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 391.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 392.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 393.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 394.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 395.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 396.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 397.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 398.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 399.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 400.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 401.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 402.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 403.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 404.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 405.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 406.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 407.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 408.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 409.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 410.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 411.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 412.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 413.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 414.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 415.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 416.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 14.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-14.csv`](cccr/D-4-01-chassis-14.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 417.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 418.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 419.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 420.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 421.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 422.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 423.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 424.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 425.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 426.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 427.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 428.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 429.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 430.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 431.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 432.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 433.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 434.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 435.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 436.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 437.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 438.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 439.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 440.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 441.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 442.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 443.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 444.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 445.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 446.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 447.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 448.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 15.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-15.csv`](cccr/D-4-01-chassis-15.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 449.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 450.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 451.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 452.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 453.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 454.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 455.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 456.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 457.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 458.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 459.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 460.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 461.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 462.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 463.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 464.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 465.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 466.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 467.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 468.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 469.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 470.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 471.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 472.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 473.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 474.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 475.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 476.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 477.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 478.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 479.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 480.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 16.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-16.csv`](cccr/D-4-01-chassis-16.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 481.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 482.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 483.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 484.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 485.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 486.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 487.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 488.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 489.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 490.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 491.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 492.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 493.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 494.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 495.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 496.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 497.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 498.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 499.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 500.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 501.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 502.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 503.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 504.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 505.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 506.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 507.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 508.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 509.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 510.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 511.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 512.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 17.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-17.csv`](cccr/D-4-01-chassis-17.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 513.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 514.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 515.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 516.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 517.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 518.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 519.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 520.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 521.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 522.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 523.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 524.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 525.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 526.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 527.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 528.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 529.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 530.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 531.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 532.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 533.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 534.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 535.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 536.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 537.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 538.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 539.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 540.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 541.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 542.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 543.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 544.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 18.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-18.csv`](cccr/D-4-01-chassis-18.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 545.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 546.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 547.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 548.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 549.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 550.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 551.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 552.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 553.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 554.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 555.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 556.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 557.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 558.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 559.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 560.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 561.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 562.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 563.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 564.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 565.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 566.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 567.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 568.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 569.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 570.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 571.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 572.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 573.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 574.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 575.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 576.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 19.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-19.csv`](cccr/D-4-01-chassis-19.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 577.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 578.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 579.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 580.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 581.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 582.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 583.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 584.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 585.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 586.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 587.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 588.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 589.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 590.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 591.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 592.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 593.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 594.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 595.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 596.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 597.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 598.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 599.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 600.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 601.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 602.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 603.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 604.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 605.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 606.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 607.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 608.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 20.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-20.csv`](cccr/D-4-01-chassis-20.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 609.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 610.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 611.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 612.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 613.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 614.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 615.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 616.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 617.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 618.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 619.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 620.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 621.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 622.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 623.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 624.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 625.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 626.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 627.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 628.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 629.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 630.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 631.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 632.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 633.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 634.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 635.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 636.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 637.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 638.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 639.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 640.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 21.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-21.csv`](cccr/D-4-01-chassis-21.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 641.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 642.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 643.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 644.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 645.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 646.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 647.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 648.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 649.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 650.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 651.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 652.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 653.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 654.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 655.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 656.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 657.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 658.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 659.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 660.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 661.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 662.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 663.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 664.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 665.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 666.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 667.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 668.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 669.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 670.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 671.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 672.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 22.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-22.csv`](cccr/D-4-01-chassis-22.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 673.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 674.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 675.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 676.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 677.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 678.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 679.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 680.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 681.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 682.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 683.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 684.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 685.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 686.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 687.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 688.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 689.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 690.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 691.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 692.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 693.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 694.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 695.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 696.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 697.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 698.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 699.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 700.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 701.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 702.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 703.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 704.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 23.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-23.csv`](cccr/D-4-01-chassis-23.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 705.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 706.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 707.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 708.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 709.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 710.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 711.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 712.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 713.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 714.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 715.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 716.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 717.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 718.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 719.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 720.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 721.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 722.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 723.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 724.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 725.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 726.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 727.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 728.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 729.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 730.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 731.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 732.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 733.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 734.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 735.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 736.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 24.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-24.csv`](cccr/D-4-01-chassis-24.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 737.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 738.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 739.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 740.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 741.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 742.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 743.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 744.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 745.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 746.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 747.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 748.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 749.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 750.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 751.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 752.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 753.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 754.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 755.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 756.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 757.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 758.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 759.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 760.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 761.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 762.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 763.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 764.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 765.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 766.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 767.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 768.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 25.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-25.csv`](cccr/D-4-01-chassis-25.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 769.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 770.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 771.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 772.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 773.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 774.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 775.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 776.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 777.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 778.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 779.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 780.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 781.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 782.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 783.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 784.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 785.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 786.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 787.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 788.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 789.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 790.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 791.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 792.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 793.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 794.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 795.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 796.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 797.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 798.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 799.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 800.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 26.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-26.csv`](cccr/D-4-01-chassis-26.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 801.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 802.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 803.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 804.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 805.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 806.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 807.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 808.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 809.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 810.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 811.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 812.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 813.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 814.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 815.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 816.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 817.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 818.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 819.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 820.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 821.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 822.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 823.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 824.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 825.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 826.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 827.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 828.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 829.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 830.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 831.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 832.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 27.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-27.csv`](cccr/D-4-01-chassis-27.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 833.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 834.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 835.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 836.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 837.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 838.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 839.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 840.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 841.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 842.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 843.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 844.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 845.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 846.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 847.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 848.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 849.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 850.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 851.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 852.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 853.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 854.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 855.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 856.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 857.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 858.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 859.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 860.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 861.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 862.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 863.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 864.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 28.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-28.csv`](cccr/D-4-01-chassis-28.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 865.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 866.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 867.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 868.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 869.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 870.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 871.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 872.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 873.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 874.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 875.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 876.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 877.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 878.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 879.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 880.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 881.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 882.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 883.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 884.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 885.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 886.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 887.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 888.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 889.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 890.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 891.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 892.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 893.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 894.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 895.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 896.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 29.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-29.csv`](cccr/D-4-01-chassis-29.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 897.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 898.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 899.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 900.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 901.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 902.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 903.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 904.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 905.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 906.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 907.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 908.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 909.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 910.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 911.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 912.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 913.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 914.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 915.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 916.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 917.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 918.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 919.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 920.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 921.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 922.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 923.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 924.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 925.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 926.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 927.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 928.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 30.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-30.csv`](cccr/D-4-01-chassis-30.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 929.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 930.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 931.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 932.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 933.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 934.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 935.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 936.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 937.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 938.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 939.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 940.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 941.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 942.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 943.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 944.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 945.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 946.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 947.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 948.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 949.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 950.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 951.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 952.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 953.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 954.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 955.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 956.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 957.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 958.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 959.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 960.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 31.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-31.csv`](cccr/D-4-01-chassis-31.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 961.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 962.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 963.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 964.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 965.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 966.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 967.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 968.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 969.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 970.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 971.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 972.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 973.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 974.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 975.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 976.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 977.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 978.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 979.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 980.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 981.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 982.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 983.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 984.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 985.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 986.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 987.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 988.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 989.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 990.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 991.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 992.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 32.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-32.csv`](cccr/D-4-01-chassis-32.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see the above section 2. Preparation)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 993.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 994.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 995.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 996.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 997.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 998.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 999.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 1000.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 1001.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 1002.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 1003.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 1004.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 1005.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 1006.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 1007.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 1008.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 1009.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 1010.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 1011.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 1012.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 1013.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 1014.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 1015.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 1016.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 1017.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 1018.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 1019.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 1020.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 1021.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 1022.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 1023.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 1024.  Verify that the AC response conform to the Expected Response as listed above.
1. Load CCCR [`D-4-01-all-channels.csv`](cccr/D-4-01-all-channels.csv)  (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
1. __Collect and verify recording for 15 to 16 minutes at 1Ksps__
    1. Set sample rate to 1Ksps and enable acquisition.  (see [D.4.6](D-4-06_PROC_-_Monitoring_a_Data-Channel_in_Real_Time.md))
    1. Record for 15 to 16 minutes  (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Inspect this recording according to [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md).
    1. [_] Ensure data is complete for the entire 15 to 16 range
1. __Collect and verify recording for 15 to 16 minutes at 5Ksps__
    1. Set sample rate to 5Ksps and enable acquisition.  (see [D.4.6](D-4-06_PROC_-_Monitoring_a_Data-Channel_in_Real_Time.md))
    1. Record for 15 to 16 minutes  (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Inspect this recording according to [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md).
    1. [_] Ensure data is complete for the entire 15 to 16 range
1. __Collect and verify recording for 15 to 16 minutes at 25Ksps__
    1. Set sample rate to 25Ksps and enable acquisition.  (see [D.4.6](D-4-06_PROC_-_Monitoring_a_Data-Channel_in_Real_Time.md))
    1. Record for 15 to 16 minutes  (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Inspect this recording according to [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md).
    1. [_] Ensure data is complete for the entire 15 to 16 range
1. __Collect and verify recording for 15 to 16 minutes at 50Ksps__
    1. Set sample rate to 50Ksps and enable acquisition.  (see [D.4.6](D-4-06_PROC_-_Monitoring_a_Data-Channel_in_Real_Time.md))
    1. Record for 15 to 16 minutes  (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Inspect this recording according to [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md).
    1. [_] Ensure data is complete for the entire 15 to 16 range
1. Power off chassis 9 through 32
1. Set sample rate to 250Ksps and enable acquisition.  (see [D.4.6](D-4-06_PROC_-_Monitoring_a_Data-Channel_in_Real_Time.md))
1. Chassis 1.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-01.csv`](cccr/D-4-01-chassis-01.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see Preparation above)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 1.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 2.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 3.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 4.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 5.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 6.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 7.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 8.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 9.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 10.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 11.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 12.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 13.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 14.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 15.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 16.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 17.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 18.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 19.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 20.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 21.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 22.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 23.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 24.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 25.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 26.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 27.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 28.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 29.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 30.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 31.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 32.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 2.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-02.csv`](cccr/D-4-01-chassis-02.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see Preparation above)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 33.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 34.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 35.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 36.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 37.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 38.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 39.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 40.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 41.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 42.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 43.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 44.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 45.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 46.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 47.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 48.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 49.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 50.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 51.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 52.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 53.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 54.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 55.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 56.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 57.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 58.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 59.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 60.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 61.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 62.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 63.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 64.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 3.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-03.csv`](cccr/D-4-01-chassis-03.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see Preparation above)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 65.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 66.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 67.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 68.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 69.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 70.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 71.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 72.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 73.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 74.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 75.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 76.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 77.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 78.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 79.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 80.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 81.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 82.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 83.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 84.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 85.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 86.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 87.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 88.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 89.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 90.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 91.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 92.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 93.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 94.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 95.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 96.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 4.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-04.csv`](cccr/D-4-01-chassis-04.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see Preparation above)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 97.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 98.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 99.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 100.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 101.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 102.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 103.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 104.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 105.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 106.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 107.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 108.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 109.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 110.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 111.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 112.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 113.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 114.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 115.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 116.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 117.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 118.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 119.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 120.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 121.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 122.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 123.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 124.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 125.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 126.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 127.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 128.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 5.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-05.csv`](cccr/D-4-01-chassis-05.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see Preparation above)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 129.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 130.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 131.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 132.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 133.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 134.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 135.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 136.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 137.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 138.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 139.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 140.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 141.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 142.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 143.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 144.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 145.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 146.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 147.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 148.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 149.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 150.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 151.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 152.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 153.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 154.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 155.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 156.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 157.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 158.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 159.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 160.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 6.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-06.csv`](cccr/D-4-01-chassis-06.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see Preparation above)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 161.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 162.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 163.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 164.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 165.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 166.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 167.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 168.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 169.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 170.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 171.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 172.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 173.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 174.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 175.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 176.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 177.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 178.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 179.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 180.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 181.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 182.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 183.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 184.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 185.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 186.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 187.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 188.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 189.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 190.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 191.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 192.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 7.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-07.csv`](cccr/D-4-01-chassis-07.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see Preparation above)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 193.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 194.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 195.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 196.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 197.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 198.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 199.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 200.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 201.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 202.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 203.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 204.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 205.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 206.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 207.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 208.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 209.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 210.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 211.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 212.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 213.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 214.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 215.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 216.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 217.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 218.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 219.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 220.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 221.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 222.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 223.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 224.  Verify that the AC response conform to the Expected Response as listed above.
1. Chassis 8.  Connect signal generator.
    1. [_] Ensure successful DC calibration ([D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md)) of all 32 channels.
    1. Load CCCR [`D-4-01-chassis-08.csv`](cccr/D-4-01-chassis-08.csv) (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
    1. Configure/restore function generator for 9KHz Sine (see Preparation above)
    1. Collect recording for 10 - 20 seconds (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Open recording in Viewer (see [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md))
        - [ ] Channel 1, signal 225.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 2, signal 226.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 3, signal 227.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 4, signal 228.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 5, signal 229.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 6, signal 230.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 7, signal 231.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 8, signal 232.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 9, signal 233.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 10, signal 234.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 11, signal 235.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 12, signal 236.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 13, signal 237.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 14, signal 238.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 15, signal 239.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 16, signal 240.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 17, signal 241.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 18, signal 242.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 19, signal 243.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 20, signal 244.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 21, signal 245.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 22, signal 246.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 23, signal 247.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 24, signal 248.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 25, signal 249.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 26, signal 250.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 27, signal 251.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 28, signal 252.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 29, signal 253.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 30, signal 254.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 31, signal 255.  Verify that the AC response conform to the Expected Response as listed above.
        - [ ] Channel 32, signal 256.  Verify that the AC response conform to the Expected Response as listed above.
1. Load CCCR [`D-4-01-256-channels.csv`](cccr/D-4-01-256-channels.csv)  (see [D.4.4](D-4-04_PROC_-_Per_Test_User_Configuration_Procedure.md))
1. Collect recording for 15 minutes at 250Ksps
    1. Set sample rate to 250Ksps and enable acquisition.  (see [D.4.6](D-4-06_PROC_-_Monitoring_a_Data-Channel_in_Real_Time.md))
    1. Record for 15 to 16 minutes  (see [D.4.5](D-4-05_PROC_-_Making_a_Recording_Procedure.md))
    1. Inspect this recording according to [D.4.7](D-4-07_PROC_-_Review_Previously_Recorded_Data.md).
    1. [_] Data is complete for entire time range
1. Export this recording according to [D.4.8](D-4-08_PROC_-_Export_Data_from_the_System.md).
    1. [_] Export as UFF58b
    1. [_] Verify exported UFF58b file
    1. [_] Export as CSV
    1. [_] Verify exported CSV file
1. Execute Cleanup section of [D.4.2](D-4-02_PROC_-_Measurement_Device_Calibration.md).
1. If applicable, run through the "System Power Down" section of [D.4.3](D-4-03_PROC_-_Start-up_and_Shut-down.md).

## 5. References

- Quartz [functional test](https://github.com/osprey-dcs/quartz-daq-250-24/blob/master/documentation/functional-testing.md#alias-rejection-testing)
report.

## 6. Start/Completion Validation

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
