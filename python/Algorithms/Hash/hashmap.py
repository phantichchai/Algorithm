class Solution:
    def frequencySort(self, s: str) -> str:
        # create the temperal dic for contain a key-value pair between unique character and frequency
        frequencies = {}
        
        # iterate though sting 's' for counting frequency fo each character 
        # then map the key is unique character with counting number of occurence
        for c in s:
            frequencies[c] = 1 + frequencies.get(c, 0)
        
        # create empty string 'output' for return the answer    
        output = ""
        
        # sorted the dic by value as descending order
        # then iterate though the sorted new dic and build the string 'output' from key char multipy by frequency
        for char in dict(sorted(frequencies.items(), key=lambda item: item[1], reverse=True)):
            output += char * frequencies[char]
            
        # then return the string output
        return output