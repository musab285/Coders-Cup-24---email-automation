from datetime import datetime
from sendAttachedMail_invalid import sendAttachmentMail
from csvWriter import writeRecordsToCsv, readRecordsFromCsv, readRecordsFromExcel
from emailHtmlContent_Invalid import getHtmlContent
import easygui

# this is for invalid vjudge usernames

print("==================================================================")
print("         CODER'S CUP VJUDJE WARNING AUTOMATION 2024 ")
print("==================================================================\n")

# TODO replace with master csv in case of cron jobs
dataCsvPath = easygui.fileopenbox()

unsentMailsCsvPath = "unsentRecords.csv"
sentMailsCsvPath = "sentRecords.csv"
processLogFilePath = "processLogs.log"

# Opening Log File
processLogFile = open(processLogFilePath, "a")

unsentRecords = readRecordsFromCsv(dataCsvPath)
print(f"Unsent Records: {unsentRecords}")
sentRecords = readRecordsFromCsv(sentMailsCsvPath)

totalRecords = len(unsentRecords)
unsentLength = totalRecords

processLogFile.write(f"{datetime.now()} : PROCESS STARTED\n")

try:

    i = 0

    while i < unsentLength:
        memberData = unsentRecords[i]
        
        tabledata = [
                {"Name": memberData.get("Leader Name", "Unknown"), "ID": memberData.get("Leader ID", 0)},
                {"Name": memberData.get("mem1Name", "Unknown"), "ID": memberData.get("mem1Id", 0)},
                {"Name": memberData.get("mem2Name", "Unknown"), "ID": memberData.get("mem2Id", 0)}
                ]
        
        # Define your date in the format YYYY-MM-DD
        date_str = memberData.get("Date", "unknown")


        # Convert the string to a datetime object
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")

        # Format the date in words
        formatted_date = date_obj.strftime("%B %d, %Y")
        Day = memberData.get("Day", "unknown")
        Time = memberData.get("Time", "unknown")
        Venue = memberData.get("Venue", "unknown")
        attendance_code = memberData.get("Attendance Code", "unknown")

        htmlContent = getHtmlContent(memberData["Team Name"], formatted_date, Day, Time, Venue, attendance_code, tabledata)

        # sort the data according to if the mail was sent or not
        if (
            sendAttachmentMail(memberData["Leader Email"], htmlContent)
            == True
        ):
            unsentRecords.remove(memberData)
            sentRecords.append(memberData)
            processLogFile.write(f"{datetime.now()} : SUCCESSFULLY SENT TO {memberData["Leader Email"]}\n")
            i -= 1
            unsentLength -= 1
        else:
            processLogFile.write(f"{datetime.now()} : FAILED TO SEND TO {memberData["Leader Email"]}\n")
        i += 1


except Exception as ex:
    print("[!] AN ERROR OCCOURED:-")
    processLogFile.write(f"""{datetime.now()} : EXCEPTION OCCOURED\n\t{ex}\n""")
    print(ex)

finally:

    print("[+] Writing data to files before exiting...")

    if writeRecordsToCsv(sentRecords, sentMailsCsvPath):
        print("   [+] Sent records written to file")
    else:
        print("   [+] No sent records to write.")

    if writeRecordsToCsv(unsentRecords, unsentMailsCsvPath):
        print("   [+] Unsent records written to file")
    else:
        print("   [+] No unsent records to write.")

    # Logging process end
    processLogFile.write(f"{datetime.now()} : PROCESS ENDED\n")

    # Closing log file
    processLogFile.close()

print("\n\n======== OPERATION SUMMARY ========")
print(f"\nTotal records to send: {totalRecords}")
print(f"\nSuccessful mails: {totalRecords - unsentLength}")
print(f"--> Saved in: {sentMailsCsvPath}")

print(f"\nUnsuccessful mails: {unsentLength}")
print(f"--> Saved in: {unsentMailsCsvPath}")
