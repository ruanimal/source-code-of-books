class PerformanceCalculator {
  constructor(aPerformance, aPlay) {
    this.performances = aPerformance
    this.play = aPlay
  }

  get amount() {
    throw new Error('subclass resonsibility')
  }

  get volumeCredits() {
    return Math.max(this.performances.audience - 30, 0);
  }
}

class TragedyCalculator extends PerformanceCalculator {
  get amount() {
    let result = 40000;
    if (this.performances.audience > 30) {
      result += 1000 * (this.performances.audience - 30);
    }
    return result
  }
}

class ComedyCalculator extends PerformanceCalculator {
  get amount() {
    let result = 30000;
    if (this.performances.audience > 20) {
      result += 10000 + 500 * (this.performances.audience - 20);
    }
    result += 300 * this.performances.audience;
    return result
  }

  get volumeCredits() {
    return super.volumeCredits + Math.floor(this.performances.audience / 5);
  }
}

function cratePerformanceCalculator(aPerformance, aPlay) {
  switch (aPlay.type) {
    case "tragedy": return new TragedyCalculator(aPerformance, aPlay)
    case "comedy": return new ComedyCalculator(aPerformance, aPlay)
    default: throw new Error(`unknown type: ${aPlay.type}`)
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
    const calculator = cratePerformanceCalculator(aPerformance, playFor(aPerformance))
    const result = Object.assign({}, aPerformance)
    result.play = calculator.play
    result.amount = calculator.amount
    result.volumeCredits = calculator.volumeCredits
    return result

    function playFor(aPerformance) {
      return plays[aPerformance.playID]
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
