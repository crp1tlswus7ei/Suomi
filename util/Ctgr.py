categories = [
   'Rank', 'Ban', 'Kick', 'SoftBan', 'UnBan',
   'Warns', 'UnWarn', 'ClearWarns', 'WarnList',
   'Mute', 'UnMute', 'HardMute', 'SetMute',
   'Timeout', 'UnTimeout', 'LockChannel', 'UnLockChannel',
   'Clear', 'Purge', 'CloneRole', 'MassRole'
]

def _CommandsCategories(items: list[str], cols: int = 2) -> str:
   rows = (len(items) + cols - 1) // cols
   split = [items[i * rows:(i + 1) * rows] for i in range(cols)]
   widths = [max(len(x) for x in col) + 4 for col in split]

   return '\n'.join(
      ''.join(
         col[row].ljust(widths[i])
         for i, col in enumerate(split)
         if row < len(col)
      )
      for row in range(rows)
   )

text = _CommandsCategories(categories, cols = 2)