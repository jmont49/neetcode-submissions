class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        held_temps = []
        held_indices = []
        running_times = []

        res = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while held_temps and held_temps[-1] < temperatures[i]:
                curr_ind = held_indices[-1]
                held_indices.pop()

                held_temps.pop()

                curr_time = running_times[-1]
                running_times.pop()

                res[curr_ind] = curr_time

            for j in range(len(running_times)):
                running_times[j] += 1

            held_temps.append(temperatures[i])
            held_indices.append(i)
            running_times.append(1)

        
        return res

            


                

            
        