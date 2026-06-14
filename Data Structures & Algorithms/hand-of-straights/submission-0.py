"""
    Hand of Straights
    You are given 
        - an integer array hand 
            where hand[i] is the value written on the ith card
        - and an integer groupSize

    - You want to rearrange the cards into groups so that each group is of size groupSize
    - and card values are consecutively increasing by 1.

    Return:
         true if it's possible to rearrange the cards in this way, 
         return false otherwise

    1. Notas:
        - ¿puedo repartir TODAS las cartas en paquetes de tamaño groupSize consecutivas (x, x+1, x+2...)?
        
        Importante:
            - divisibilidad: len(hand) % groupSize != 0 -> False directo
            - empezar siempre en la carta más pequeña
            - me importan las frecuencias no el orden de las cartas en hand

    2. Preguntas:
        - ¿groupSize > len(hand)? -> no
        - ¿valores repetidos? -> si
        - ¿pueden los valores ser 0 o negativos? si
        - ¿hand puede venir vacío? no

    3. Entradas y salidas:
        def isNStraightHand(self, hand:List[int], groupSize: int) -> bool:
            - hand: List[int] -> lista de valores de las cartas
            - groupSize: int -> cuántas cartas consecutivas debe tener cada grupo
            - return bool -> True si se pueden formar grupos, False si no

    4. Ejemplos:

        Example 1:
        Input: hand = [1,2,4,2,3,5,3,4], groupSize = 4

        len(hand) = 8, 8 % 4 == 0 -> ok seguimos

        frecuencias =
        {
            1: 1,
            2: 2,
            3: 2,
            4: 2,
            5: 1
        }

        min_disponible = 1 -> grupo = [1, 2, 3, 4] len = 4

        frecuencias =
        {
            1: 0,
            2: 1,
            3: 1,
            4: 1,
            5: 1
        }

        min_disponible = 2 -> grupo = [2, 3, 4, 5] len = 4

        frecuencias =
        {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0
        }

        frecuencias todo a 0 -> return True

        Output: true
        Explanation: The cards can be rearranged as [1,2,3,4] and [2,3,4,5].

    5. Approach: Greedy con min-heap

        1. Si len(hand) % groupSize != 0 → devuelvo false ya (no se puede partir parejo).
        2. Construyo count = Counter(hand) (frecuencias de cada valor) 
        3. Meto las claves únicas en un min-heap para sacar siempre 
        4. Mientras quede algo: el mínimo abre el grupo -> desde start hasta start + groupSize - 1
        5. Para cada carta del grupo si no queda -> False
            - Si queda -> descontamos una carta
        6. 





Example 2:

Input: hand = [1,2,3,3,4,5,6,7], groupSize = 4

Output: false
Explanation: The closest we can get is [1,2,3,4] and [3,5,6,7], but the cards in the second group are not consecutive.

Constraints:

1 <= hand.length <= 1000
0 <= hand[i] <= 1000
1 <= groupSize <= hand.length




"""

import heapq
from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        # count = {1: 1, 2: 2, 3: 2, 4: 2, 5: 1} -> keys: values

        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            start = min_heap[0]

            for value in range(start, start + groupSize):
                if count[value] == 0:
                    return False
                
                count[value] -= 1

                #si value es la cima del heap y se queda a 0, la retiro para mantener el orden
                if value == min_heap[0] and count[value] == 0:
                    heapq.heappop(min_heap)

        #cierre el heap sin fallar: todos los grupos se han formado correctamente
        return True







        