# Postmoterm

![postmoterm debugging](https://bit.ly/3v3Upz1)
## Issue Summary :

The outage happened from 15–02–2022 at 04 AM CT to 8 AM CT. The issue was that Apache is returning  Internal Server Error (500)  which is preventing Apache from processin a request and returning a proper response.

## Timeline :
* 8:20 AM : The issue was detected.
* 8:29 AM : After HTTP Testing, it was realized that the Apache2 web server was    unable to serve content.
* 8:35 AM : The issue escalated to the back-end team.
* 8:43 AM : Examined server using **`curl -sI …`**, the website returned Internal Server Error (status code 500)with cmd
* 8:51 AM : The error found was a typo in page file extension .phpp instead of php.
* 8:59 AM : The error was fixed and apache restarted.
* 9:05 AM : After running the command, the webserver worked as expected.

## Root Cause Resolution

The issue was caused by a typo in the settings file for Apache2. This was a typo in page file extension .phpp instead of php. That is:

**`/var/www/html/wp-includes/class-wp-locale.phpp`**, was missing but is required in the **`/var/www/html/wp-settings.php`**.

The error was fixed by using the command:

 **`sed -i ‘s/phpp/php/’ /var/www/html/wp-settings.php /var/www/html/wp-settings.php; service apache2 restart`**

## Corrective and Preventative Measures

To prevent similar problems from appearing:
* Put in place effort to test all code before deployment as well as establish code testing protocol.
* Note down changes to the configuration files.
* Put into place a web monitoring software to our servers.
