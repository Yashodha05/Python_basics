'''3. Define a dictionary called agencies that stores a mapping of acronyms CBI, FBI, NIA, 
SSB, WBA (keys) to Indian government agencies ‘Central Bureau of Investigation’, 
‘Foreign direct investment', 'National investigation agency', 'Service selection board' and 
'Works Progress administration' (the values) created by PM during new deal. Then  
a) add the map of acronym BSE "Bombay stock exchange"  
b) change the value of key SSB to social security administration  
c) Remove the pairs with keys CBI and WPA.  '''


agencies={ 
  "CBI":"Central Bureau of Investigation", 
  "FBI":"Foregin Direct Investement", 
  "NIA":"National Investigation Agency", 
  "SSB":"Service Selection Board", 
  "WPA":"Works Progress Administration", 
} 

print("Dictionary\n",agencies) 

#a.Add the map BSE 
agencies["BSE"]="Bombay Stock Exchange" 
print("Dictionary after change\n",agencies) 

#b. Change value of key SSB to Social Security Administation 
agencies["SSB"]="Social Security Administration" 
print("Dictionary after change of SSB ",agencies) 

#c. Remove the CB & WPA 
agencies.pop("CBI",None) 
agencies.pop("WPA",None) 
print("Dcitionary After Removing",agencies)
