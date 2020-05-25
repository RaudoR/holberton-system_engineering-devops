Postmortem - System failure report
Incident Summary
On the morning of Monday 25, 2020 at 10:00 A.M PST, we received a distress call of our IT department assistant supervisor about an explosion inside of the server room. This incident resulted in reduced productivity, data that we analyzed concluded on an approximate 40% decrease in our capabilities. You might be experiencing slowed response from our network and in some cases you may be unable to access some applications at all.

Timeline
10:00 A.M - A large explosion is heard inside the server room followed by a shutdown of web applications.
10:01 A.M - Our in house monitoring applications start sending notifications that our systems are severely damaged.
10:10 A.M - We evacuate the area, due to the possibility of fire inside the building.
10:30 A.M - After no fire was detected, and there was no serious damage to the building, we began to investigate the cause of the explosion, it was caused by insufficient thermal control inside the server room causing the servers to overheat.
10:40 A.M - We inform the rest of the team and our CTO of the incident, as well as all other teams that may be affected by the situation.
12:00 A.M - The damaged server was removed, we regulated the thermal control of the room to prevent it from happening again.

Cause and Resolution
The issue, like mentioned before was caused by faulty thermal regulation of the server room, the cause of this was that one of our team members failed to properly regulate the temperature, this was an isolated incident and the appropriate retraining of our team was provided to ensure the safety of our hardware and the wellbeing of our employees.


Corrective/Preventative measures
As part of our Disaster Recovery Plan (DRP) we have safeguards established to deal with this situation. No data is going to be lost, we use a RAID (Redundant Array of Independent Disks)  level 5 with fault tolerance, in short what this means is that any data written in any Hard Drive is mirrored and written in different Drives so if one fails we constantly have a backup, again No data was lost.