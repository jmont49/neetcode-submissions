class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        held_temps = []
        held_indices = []


        res = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while held_temps and held_temps[-1] < temperatures[i]:
                curr_ind = held_indices[-1]
                held_indices.pop()

                held_temps.pop()


                res[curr_ind] = i - curr_ind


            held_temps.append(temperatures[i])
            held_indices.append(i)

        
        return res

            


                

            
        