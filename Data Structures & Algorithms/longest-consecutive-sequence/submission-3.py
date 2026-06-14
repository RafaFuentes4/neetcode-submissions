"""

    Longest Consecutive Sequence
    Given an array of integers nums, 
    return the length of the longest consecutive sequence of elements that can be formed.

    A consecutive sequence is a sequence of elements in which each element is exactly 1 
    greater than the previous element. 
    The elements do not have to be consecutive in the original array.

    You must write an algorithm that runs in O(n) time.

    Example 1:

    Input: nums = [2,20,4,10,3,4,5]
    Output: 4
    Explanation: The longest consecutive sequence is [2, 3, 4, 5].

    Example 2:

    Input: nums = [0,3,2,5,4,6,1,1]

    Output: 7


    1- Notes:
        - return longitud de la secuencia consecutiva más larga
        - cada elemento es 1 mayor que el anterior: x, x+1, x+2...
        - el orden en el array original no importa: ordenación O(n * log n) o hash set consultar O(1)
        - example 2 duplicate -> set los deduplica

    2- Questions?
        1. array vacio? ¿devuelvo 0? si
        2. duplicados? si
        3. negativos? si -> set lo maneja igual
        4. devuelvo longitud o secuencia? longitud
        5. todos los numeros enteros? si

    3. Entradas y salidas:

        def longestConsecutive(self, nums: List[int]) -> int:

    4. Examples:

        - Example 1:
            nums = [2,20,4,10,3,4,5]
            nums = {2,20,4,10,3,4,5}

            inicios de racha (no existe n - 1):
                2 -> 2, 3, 4, 5 -> longitud 4 --- MAX
                10 -> 10 -> longitud 1
                20 -> 20 -> longitud 1

            return 4

"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_length = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_length = 1

                while num + current_length in num_set:
                    current_length += 1
                
                longest_length = max(longest_length, current_length)

        return longest_length






        