import abc


class MediaLoader(abc.ABC):
  @abc.abstractmethod
  def play(self) -> None:
    pass

  @property
  @abc.abstractmethod
  def exit(self) -> str:
    pass

