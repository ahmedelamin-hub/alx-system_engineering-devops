Postmortem: Web Stack Debugging Project Outage
Issue Summary

Duration:
The outage lasted for 3 hours, starting at 14:00 UTC and ending at 17:00 UTC on June 12, 2024.

Impact:
The primary web service was completely down, preventing users from accessing the application. Approximately 85% of users were affected as they were unable to log in or access any functionalities. Users experienced a "503 Service Unavailable" error across all endpoints.

Root Cause:
A misconfiguration in the load balancer settings led to an excessive number of connections being routed to a single server, causing it to overload and crash.

Timeline

14:00 UTC - Issue detected via monitoring alert indicating a spike in 503 errors.
14:05 UTC - Incident escalated to the on-call engineering team.
14:10 UTC - Initial investigation began, focusing on server health and network connectivity.
14:20 UTC - Assumed root cause was a potential DDoS attack; traffic patterns were analyzed.
14:45 UTC - Misleading path: network security team investigated potential breaches, but found no anomalies.
15:00 UTC - Web server logs reviewed; high number of requests from load balancer identified.
15:15 UTC - Load balancer configuration settings were examined.
15:30 UTC - Root cause identified: incorrect load balancer configuration causing uneven traffic distribution.
16:00 UTC - Configuration corrected, and load balancer settings were updated.
16:30 UTC - System rebooted and services gradually restored.
17:00 UTC - Full service restoration confirmed, and incident marked as resolved.
Root Cause and Resolution

Root Cause:
The load balancer was configured with an incorrect setting that directed the majority of incoming traffic to a single backend server. This server was not able to handle the load, leading to its crash and causing the service to be unavailable. The issue was not initially evident because the configuration error was subtle and required a detailed review of the load balancer settings.

Resolution:
The load balancer configuration was corrected to ensure an even distribution of traffic across all available servers. Specifically, the setting for the maximum connections per server was adjusted, and additional health checks were implemented to prevent similar issues in the future. The affected server was restarted, and the services were monitored to ensure stability before fully bringing the system back online.

Corrective and Preventative Measures

Improvements and Fixes:

Review and Audit Configuration: Regular audits of load balancer and server configurations to prevent misconfigurations.
Enhanced Monitoring: Implement more granular monitoring and alerting for load balancer performance and traffic distribution.
Documentation and Training: Update documentation on load balancer settings and conduct training sessions for the engineering team.
TODO List:

Patch Load Balancer: Apply the latest updates and patches to the load balancer software.
Add Monitoring: Implement detailed monitoring for server load and traffic distribution to catch anomalies early.
Implement Redundancy: Configure automatic failover mechanisms to ensure no single server can become a bottleneck.
Conduct Load Testing: Perform regular load testing to understand system limits and ensure resilience.
Update Documentation: Revise configuration guides and runbooks to include the latest best practices and lessons learned from this incident.
