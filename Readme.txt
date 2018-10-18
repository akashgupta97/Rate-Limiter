Prerequisites:-
	1 - Operating System:-Windows 7 or above
	2 - pip(inbuilt in python 3.4 or above)
	3 - Python 3.5 or above
        4 - Preferred IDE "Spyder 3"
	5 - cURL command line tool
	6 - Usable Main Memory minimum 2GB
	7 - Stable Internet Connection
 
How to Install:-
1.Python 3.5
	1 - Go to URL https://www.python.org/downloads/windows/
	2 - Download "Windows x86-64 executable installer"
	3 - Install the downloaded file

2.cURL command line tool
	1 - Go to URL https://curl.haxx.se/dlwiz/
	2 - Select Type of Package: curl executable
	3 - Select Operating System: Win64
	4 - Select for What Flavour: Generic
	5 - Select which Win64 version: Any
	6 - Select for What CPU: x86_64
	7 - Install or unzip, find curl.exe

3. How to install pip:
	1 - Type on your command line "curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py"
	2 - Then type "python get-pip.py"

How to set path of cURL:-
	1 - From the Desktop, right-click My Computer and click Properties.
	2 - Click Advanced System Settings .
	3 - In the System Properties window click the Environment Variables button.
	4 - Select Path and click Edit.
	5 - Append ;c:\path to curl directory at the end.
	5 - Click OK.
	6 - Close and re-open the command prompt.
	

Input:-
  1 - Input Format is .csv
  2 - Input consists of firstname , lastname and location of user of multiple users, ensure that the first alphabets of all three are in capitals, and in case of no location provided, leave it blank, i.e.
      nothing empty like "".
  3 - The name of the input csv file MUST be 'input.csv', the program is hardcoded to only detect this name.
  4 - In case there are more than 14670 developer combinations (first name, last name, location) , please break the data into two csv files and run the process one by one for both the files.


Output:-
  1 - Output Format is .csv, alongwith the same data being provided in a txt file too.
  2 - There can be multiple usernames which corresponds to given combination of firstname, lastname and location. 
  3 - The output will show the details of all the usernames which corresponds to the given combination.   
  4 - Output consists of profile details
	1. login
	2. id
	3. name
	4. location
	5. number of public repos
	6. followers 
	7. created_at (account creation)
	8. Name of repositories where they are contributing
	9. No. of commits made by that user on those repositories
	More account details were possible to be presented as well. 9 details were chosen on purpose.
The output in csv has location specified as "world" where location is not specified in the input file.
Viewing output in excel is also possible, since it is a csv file, BUT,not if the number of inputs are more than 1500 developers, since Excel has a limit of 65535 rows.
BUT it can still be viewed as a csv(FinalResult.csv), and also as a txt file(outp.txt)
Developers that have 0 repositories,have been displayed at the end of the csv output.

Execution instructions:
1. Unzip the file.
2. After unzipping our submission, place the input file(adhering to the input format and constraint) in the single folder that will come out. 
3. Delete outp.txt and then run blue_final.py(preferably in Spyder)
4. During the execution of the process, there might be multiple(~100)terminal windows popping up every now and then.This might be quite domination but do not close the windows, 
   as they are curl requests to api.github.com
5. Just in case there are files of the name : issues.txt, or issunoc.txt, issurep.txt, rep_list.txt.,pdata.txt These are to be deleted before the execution of the program, otherwise there
  might be duplication of data.
6. blue_final.py just needs input.csv, csvconv.py and blue_lib.py to work in any directory anywhere as long as the system is connected to internet.

Caution:
1 - If "The process cannot access the file because it is being used by another process" error arises, then your internet speed is slow. Please check your internet connection.
2 - Do not delete speed_factor.txt!
3 - Very slow internet speed can lead to program crash (less than 300kbps)
4 - The path to the blue_final.py file should not have any spaces in it. e.g. a folder name like "blue optima" will cause failure in command execution, kindly rename it to "blue_optima" for the meanwhile
5 - Generate your own access token by Outh2 Authentication. 
    Link:-https://developer.github.com/v3/