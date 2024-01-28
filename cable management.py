import heapq

# Приклад довжин кабелю
cable_lengths = [2, 5, 8, 13]
print(f" Довжини кабелю: {cable_lengths}")


def min_cost_to_combine_cables(lengths):
    heapq.heapify(lengths)
    # створюємо мінімаьну купу з довжин кабелів
    total_cost = 0

    while len(lengths) > 1:
        # Вибираємо два кабелі з найменшою довжиною
        first = heapq.heappop(lengths)
        second = heapq.heappop(lengths)

        # Об'єднуємо ці кабелі
        combined_lengths = first + second

        total_cost += first + second
        # Повертаємо результат об'єднання назад у купу
        heapq.heappush(lengths, combined_lengths)
        print(
            f"Об'єднуємо {first} і {second}, витрати: {combined_lengths}, загальні витрати: {total_cost}")

    return total_cost


print(f" Total cost: {min_cost_to_combine_cables(cable_lengths)}")
