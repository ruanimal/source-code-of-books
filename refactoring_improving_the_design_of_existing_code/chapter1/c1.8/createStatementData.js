class PerformanceCalculator {
  constructor(aPerformance, aPlay) {
    this.performances = aPerformance
    this.play = aPlay
  }

  get amount() {
    let result = 0;
    switch (this.play.type) {
    case "tragedy":
      result = 40000;
      if (this.performances.audience > 30) {
        result += 1000 * (this.performances.audience - 30);
      }
      break;
    case "comedy":
      result = 30000;
      if (this.performances.audience > 20) {
        result += 10000 + 500 * (this.performances.audience - 20);
      }
      result += 300 * this.performances.audience;
      break;
      default:
          throw new Error(`unknown type: ${this.play.type}`);
    }
    return result
  }

  get volumeCredits() {
    let result = 0;
    result += Math.max(this.performances.audience - 30, 0);
    if ("comedy" === this.play.type) {
      result += Math.floor(this.performances.audience / 5);
    }
    return result
  }
}

function createStatementData(invoice, plays) {
  const result =  {}
  result.customer = invoice.customer
  result.performances = invoice.performances.map(enrichPerformance)
  result.totalVolumeCredits = totalVolumeCredits(result)
  result.totalAmount = totalAmount(result)
  return result

  function enrichPerformance(aPerformance) {
    const calculator = new PerformanceCalculator(aPerformance, playFor(aPerformance))
    const result = Object.assign({}, aPerformance)
    result.play = calculator.play
    result.amount = calculator.amount
    result.volumeCredits = calculator.volumeCredits
    return result

    function playFor(aPerformance) {
      return plays[aPerformance.playID]
    }
    function amountFor(aPerformance) {
      return new PerformanceCalculator(aPerformance, playFor(aPerformance)).amount
    }
    function volumeCreditsFor(perf) {
      return new PerformanceCalculator(aPerformance, playFor(aPerformance)).volumeCredits
    }
  }
  function totalVolumeCredits(data) {
    return data.performances.reduce((total, p) => total + p.volumeCredits, 0)
  }
  function totalAmount(data) {
    return data.performances.reduce((total, p) => total + p.amount, 0)
  }
}
module.exports = createStatementData;
