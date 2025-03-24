# NASA GRC-ATF FDAS D.4.2 - System Power Up/Down Procedures

Covers global system power down and up, as well as system recovery after individual chassis power cycle.

## Note on Computer Shutdown

Each computer may be requested to shutdown gracefully by one of the following methods

- Press and quickly release power button.  See Reference photos section below for button locations.
- Issue a `sudo poweroff`
- For Workstations only.  Select `Shutdown` from the system menu (lower left corner)

## System Power Down

Preparation for partial/total power outage.

If possible, save open documents on Workstations.

1. Switch off power to all 32x Quartz Chassis in the Instrument room
1. Initiate a graceful shutdown of each computer by one of the means listed above.
    1. DAQS server (Instrument room)
    1. MISC server (Control room)
    1. Workstation 1 (Control room)
    1. Workstation 2 (Control room)
1. Wait for computers to complete normal shutdown.
    - Indicated by power LEDs turning off
    - If this takes more than 5 minutes, endeavor to contact support
    - If support is unavailable in the available time,
      press and hold power button until LEDs turn off.
      (__Caution__, may result in data loss)

## System Power Up

Recovery from partial/total power outage.

1. Verify power to:
   - Control room switch (visible from front)
   - Instrument room switch (visible from rear)
   - Instrument room Time Server
1. Wait for Time Server lock
   - GPS Status should show: `IN: GPS` and `GPS: LOCK`
   - Current UTC time incrementing
1. Press and quickly release power buttons on computers
    - DAQS server
    - MISC server
    - Workstation 1
    - Workstation 2
1. Switch on power to all Quartz Chassis
1. Verify Workstation boot (repeat for each)
    1. Connect KVM console to Workstation 1 or 2
    1. Should see Desktop (autologin to default user)
    1. Use the icon on Desktop to launch the `Phoebus` application.
    1. Select the `Main` tab.
1. Check that the Archiver is running
    1. Click on the "EPICS Archiver Application" desktop icon
    1. (Alternate) Open a web browser and navigate to `http://192.168.83.101:17665/mgmt/ui/reports.html`
    1. Click on `Reports` and select `Currently disconnected PVs`
    1. Notify support if result table has entries other than: "no data found"
1. Proceed to [Inspecting the Current State and Health](healthcheck.md) of the system.

## References

Location of DAQS server power button location.

![DAQ Server Power Button](image/daqs-power.jpg)

Location of power buttons for MISC and Workstations.

![Computer room Power Buttons](image/cr-power.jpg)

Time Server front panel.

![Time Server front](image/time-front.jpg)

Quartz chassis Front and Rear panels.

![Quartz front panel](image/quartz-front.jpg)

![Quartz rear panel](image/quartz-rear.jpg)

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
