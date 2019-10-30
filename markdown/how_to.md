# 프로젝트에 포함되어야 하는 부분



## Backtesting Method(Evaluation)

- 알고리즘 트레이딩 시스템의 성능을 평가
- 다양한 방법이 있다
  - Profit / Loss
  - Hit Ratio
  - Drawdown
  - Sharpe Ratio

## Environment for Backtesting

- 데이터 긁어오기
  - 일단위 주가 : 해결됨
  - 분단위 주가 : 증권사 API를 붙여서.. 아직 해결 안됨
- 트레이딩 알고리즘 평가를 위한 패키지가 있음
  - [zipline](https://wikidocs.net/2874)

## Risk Management

- 자산을 얼마나 유지하고, 얼마를 배팅할 것인가?

## Modeling

- Input 데이터를 무엇을 받을지?
- 어떤 모델을 어떻게 사용할지?
  - Weight Agnostic NN ?
  - DQN으로써의 활용가능성 ?
    - 문제를 어떻게 정의하느냐에 따라서 강화학습으로 할 필요가 없을수도?
    - 레이블이 존재할수도 있다 (e.g. 5일 뒤 상승/하락으로 놓으면 레이블을 생성할 수 있음)
    - 이 경우에는 reward function을 design해야 할 필요가 없다

## Data

- 어떤 데이터가 어떤 종목의 주가에 영향을 줄까?
  - e.g.) 미세먼지 농도 -> 웅진코웨이

## References

- 파이썬으로 배우는 알고리즘 트레이딩 : wikidocs](https://wikidocs.net/book/110)
- [Weight Agnostic NN : Blog](https://weightagnostic.github.io)
- [Weight Agnostic NN : GitHub](https://github.com/weightagnostic/weightagnostic.github.io)
- [Weight Agnostic NN : GItHub, Release](https://github.com/google/brain-tokyo-workshop/tree/master/WANNRelease)