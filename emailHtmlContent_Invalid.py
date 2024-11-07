
def getHtmlContent(TeamName, Date, Day, Time, Venue, attendance_code, tableData):
    tableContent = ""
    for member in tableData:
        if member["Name"] != "":
            tableContent += f'''
                        <tr>
                        <td style="padding:10px;text-align:left;border:1px solid #5c696c;color:#ffffff">{member["Name"]}</td>
                        <td style="padding:10px;text-align:left;border:1px solid #5c696c;color:#ffffff">{member["ID"]}</td>
                        </tr>
                        '''
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Competition Details for Coder's Cup</title>
    </head>
    <body style="margin: 0; padding: 0; background-color: transparent; font-family: Arial, Helvetica, sans-serif;">
        <!-- Main Table Container -->
        <table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="background-color: linear-gradient(to bottom right, #0e1b2d, #1a2d4d);">
            <tr>
                <td align="center" style="padding: 20px;">
                    <!-- Content Container -->
                    <table role="presentation" cellpadding="0" cellspacing="0" width="600" style="max-width: 600px; background-color: #141f34; border-radius: 10px;">
                        <!-- Header with 3 Images -->
                        <tr>
                            <td align="center" style="padding: 20px;">
                                <table role="presentation" cellpadding="0" cellspacing="0" width="100%">
                                    <tr>
                                        <!-- First Image (FAST Logo) -->
                                        <td align="center" width="33.33%" style="padding: 10px;">
                                            <img src="https://i.ibb.co/Smx8F5D/ACM-logo-2.png" alt="ACM Logo" width="75" style="display: block; max-width: 120px;">
                                        </td>
                                        <!-- Second Image (Coders Cup Logo) -->
                                        <td align="center" width="33.33%" style="padding: 10px;">
                                            <img src="https://res.cloudinary.com/dm1xi8zff/image/upload/v1729964433/coders-cup-logo_n2cwdl.png" alt="Coders Cup Logo" width="85" style="display: block; max-width: 120px;">
                                        </td>
                                        <!-- Third Image (ACM Logo) -->
                                        <td align="center" width="33.33%" style="padding: 10px;">
                                            <img src="https://i.ibb.co/zGMKp79/nu-logo-white.png" alt="NUCES Logo" width="70" style="display: block; max-width: 120px;">
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>

                        <!-- Content -->
                        <tr>
                            <td style="padding: 0 20px;">
                                <p style="color: #ffffff; line-height: 1.6; font-family: Arial, Helvetica, sans-serif;">Dear Team <strong>{TeamName}</strong>,</p>
                                
                                <p style="color: #ffffff; line-height: 1.6; font-family: Arial, Helvetica, sans-serif;">Welcome to this year’s Coder's Cup! Below, you’ll find essential details for the event and an important action regarding your Vjudge username:</p>

                                <p style="color: #ffffff; line-height: 1.6; font-family: Arial, Helvetica, sans-serif;"><strong>Action Required:</strong> Update Your Vjudge Username</p>

                                p style="color: #ffffff; line-height: 1.6; font-family: Arial, Helvetica, sans-serif;">It has come to our attention that your team submitted an incorrect or inappropriate Vjudge username. To ensure your participation, please provide a valid username. Teams failing to update their username will be disqualified.</p>

                                <p style="color: #ffffff; line-height: 1.6; font-family: Arial, Helvetica, sans-serif;">To create a new Vjudge account, please refer to this guide: https://youtu.be/aMNqSRqdYWQ.<br>After verification of your Vjudge Username, please submit your updated username via this Google Form: https://forms.gle/5QyibjQGFqT4Mkj86.</p>
                                
                                <p style="color: #ffffff; line-height: 1.6; font-family: Arial, Helvetica, sans-serif;">Event Date: {Date} <br>Day: {Day} <br>Time: {Time} <br>Venue: {Venue} </p> 
                                
                                <p style="color: #ffffff; line-height: 1.6; font-family: Arial, Helvetica, sans-serif;">Attendance Code: <strong>{attendance_code} </strong></p>

                                <p style="color: #ffffff; line-height: 1.6; font-family: Arial, Helvetica, sans-serif;">To mark your attendance, please visit our website at the time of the competition and enter the code here: http://attendance.acmnuceskhi.com</p>

                                <p style="color: #ffffff; line-height: 1.6; font-family: Arial, Helvetica, sans-serif;">Important: You must be present in the vicinity of the lab, and attendance can only be marked during the competition timeframe.</p>

                                <p style="color: #ffffff; line-height: 1.6; font-family: Arial, Helvetica, sans-serif;">Additionally, if you arrive more than 15 minutes after the scheduled time, you will not be allowed to participate and will be considered disqualified.</p>

                                <p style="color: #ffffff; line-height: 1.6; font-family: Arial, Helvetica, sans-serif;">We look forward to seeing you there. Let’s make this an unforgettable event!</p>
                                
                                <h2 style="color: #00b7c2; font-family: Arial, Helvetica, sans-serif;">Team Details</h2>
                                
                                <!-- Team Details Table -->
                                <table role="presentation" width="100%" style="border-collapse: separate; border-spacing: 0; margin: 20px 0; border: 1px solid #5c696c;">
                                    <thead>
                                        <tr>
                                            <th style="background-color: #243b5c; color: #00b7c2; padding: 10px; text-align: left; border: 1px solid #5c696c;">Name</th>
                                            <th style="background-color: #243b5c; color: #00b7c2; padding: 10px; text-align: left; border: 1px solid #5c696c;">ID</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {tableContent}
                                    </tbody>
                                </table>
                            </td>
                        </tr>

                        <!-- Footer -->
                        <tr>
                            <td style="padding: 20px; text-align: center;">
                                <p style="color: #aaaaaa; font-size: 12px; margin: 0;">
                                    © 2024 ACM NUCES Karachi | 
                                    <a href="mailto:acm.khi@nu.edu.pk" style="color: #00b7c2; text-decoration: none;">acm.khi@nu.edu.pk</a>
                                </p>
                                
                                <!-- Social Links -->
                                <table role="presentation" cellpadding="0" cellspacing="0" style="width: 100%; margin: 15px 0;">
                                    <tr>
                                        <td align="center">
                                            <a href="https://www.facebook.com/acmnuceskhi/" style="text-decoration: none; display: inline-block; margin: 0 10px;">
                                                <img src="https://img.icons8.com/?size=100&id=118467&format=png&color=FFFFFF" alt="Facebook" width="20" height="20" style="display: inline-block;">
                                            </a>
                                            <a href="https://www.linkedin.com/company/acmnuceskhi/" style="text-decoration: none; display: inline-block; margin: 0 10px;">
                                                <img src="https://img.icons8.com/?size=100&id=8808&format=png&color=FFFFFF" alt="LinkedIn" width="20" height="20" style="display: inline-block;">
                                            </a>
                                            <a href="https://www.instagram.com/acmnuceskhi/" style="text-decoration: none; display: inline-block; margin: 0 10px;">
                                                <img src="https://img.icons8.com/?size=100&id=32309&format=png&color=FFFFFF" alt="Instagram" width="20" height="20" style="display: inline-block;">
                                            </a>
                                        </td>
                                    </tr>
                                </table>
                                
                                <p style="margin: 10px 0;">
                                    <a href="http://coderscup.acmnuceskhi.com" style="color: #00b7c2; text-decoration: none;">Visit our website</a>
                                </p>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </body>
    </html>    '''
