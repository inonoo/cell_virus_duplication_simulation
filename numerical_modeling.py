import random
from dataclasses import dataclass

@dataclass
class Cell():
  virus: int
  virus_duplication_prob: float = 0.88
  virus_equal_splitting_prob: float = 0.84

  def duplicate(self):
    daughter1, daughter2 = 0, 0
    for i in range(self.virus):
      if random.random() < self.virus_duplication_prob:
        if random.random() < self.virus_equal_splitting_prob:
          daughter1 += 1
          daughter2 += 1
        else:
          if random.random() < 0.5:
            daughter1 += 2
          else:
            daughter2 += 2
      else:
        if random.random() < 0.5:
          daughter1 += 1
        else:
          daughter2 += 1
    return (Cell(virus=daughter1,
                virus_duplication_prob=self.virus_duplication_prob,
                virus_equal_splitting_prob=self.virus_equal_splitting_prob),
            Cell(virus=daughter2,
                virus_duplication_prob=self.virus_duplication_prob,
                virus_equal_splitting_prob=self.virus_equal_splitting_prob))
pop = [Cell(virus=5)]
pop = [c.duplicate() for c in pop]
print(pop)