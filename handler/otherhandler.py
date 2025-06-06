def build_conic_gradient(values, colors):
        total = sum(values)
        conic_parts = []
        current = 0
        for value, color in zip(values, colors):
            percent = (value / total) * 100 if total else 0
            start = current
            end = current + percent
            conic_parts.append(f"{color} {start:.2f}% {end:.2f}%")
            current = end
        return ", ".join(conic_parts)