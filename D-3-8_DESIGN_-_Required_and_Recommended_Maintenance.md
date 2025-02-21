# NASA GRC-ATF FDAS D.3.8 - Required and Recommended Maintenance

For each digitizer chassis, computer and switch:
* Check the intake and exhaust fans are spinning, annually
* Clean fan filters, every 5 years
    * Power down chassis
    * Remove filters
    * Blow off dust with compressed air
    * Wash with mild soap and water
    * Reinstall
* Replace chassis fans every 6-7 years

For each computer (DAQS, MISCS, DISWS1, DISWS2):
* Check Redundant Array of Independent Disks (RAID) array status, monthly
```
$ sudo mdadm –detail /dev/md0
```
Should see [UU] for healthy, otherwise [U_] or [_U]

* Check disk usage for each partition (whether use is 90% or higher)
```
$ df -h
```
