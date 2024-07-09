class Solution:
    def reformatDate(self, date: str) -> str:
        #month = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        
        ans = ""
        
        date = date.split(" ")
        
        ans += date[2]
        ans += "-"
        
        #ans += month[date[1]]
        
        if date[1] == "Jan":
            ans += "01"
        elif date[1] == "Feb":
            ans += "02"
        elif date[1] == "Mar":
            ans += "03"
        elif date[1] == "Apr":
            ans += "04"
        elif date[1] == "May":
            ans += "05"
        elif date[1] == "Jun":
            ans += "06"
        elif date[1] == "Jul":
            ans += "07"
        elif date[1] == "Aug":
            ans += "08"
        elif date[1] == "Sep":
            ans += "09"
        elif date[1] == "Oct":
            ans += "10"
        elif date[1] == "Nov":
            ans += "11"
        elif date[1] == "Dec":
            ans += "12"
            
        ans += "-"
        
        date[0] = date[0][:-2]
        if len(date[0]) == 1:
            ans += "0"
        ans += date[0]
        
        return ans