const plays = {
  "hamlet": {"name": "Hamlet", "type": "tragedy"},
  "as-like": {"name": "As You Like It", "type": "comedy"},
  "othello": {"name": "Othello", "type": "tragedy"}
}

const invoices = [
  {
    "customer": "BigCo",
    "performances": [
      {
        "playID": "hamlet",
        "audience": 55
      },
      {
        "playID": "as-like",
        "audience": 35
      },
      {
        "playID": "othello",
        "audience": 40
      }
    ]
  }
]


function statement(invoice, plays) {
  const statementData =  {}
  statementData.customer = invoice.customer
  statementData.performances = invoice.performances.map(enrichPerformance)
  statementData.totalVolumeCredits = totalVolumeCredits(statementData)
  statementData.totalAmount = totalAmount(statementData)
  return renderPlainText(statementData)

  function enrichPerformance(aPerformance) {
    const result = Object.assign({}, aPerformance)
    result.play = playFor(result, plays)
    result.amount = amountFor(result)
    result.volumeCredits = volumeCreditsFor(result)
    return result

    function playFor(aPerformance, plays) {
      return plays[aPerformance.playID]
    }
    function amountFor(aPerformance) {
      let result = 0;
      switch (aPerformance.play.type) {
      case "tragedy":
        result = 40000;
        if (aPerformance.audience > 30) {
          result += 1000 * (aPerformance.audience - 30);
        }
        break;
      case "comedy":
        result = 30000;
        if (aPerformance.audience > 20) {
          result += 10000 + 500 * (aPerformance.audience - 20);
        }
        result += 300 * aPerformance.audience;
        break;
        default:
            throw new Error(`unknown type: ${aPerformance.play.type}`);
      }
      return result
    }
    function volumeCreditsFor(perf) {
      let result = 0;
      result += Math.max(perf.audience - 30, 0);
      if ("comedy" === perf.play.type) {
        result += Math.floor(perf.audience / 5);
      }
      return result
    }
  }
  function totalVolumeCredits(data) {
    return data.performances.reduce((total, p) => total + p.volumeCredits, 0)
  }
  function totalAmount(data) {
    return data.performances.reduce((total, p) => total + p.amount, 0)
  }
}

function renderPlainText(data) {
  let result = `Statement for ${data.customer}\n`;
  for (let perf of data.performances) {
    result += ` ${perf.play.name}: ${usd(perf.amount)} (${perf.audience} seats)\n`;
  }
  result += `Amount owed is ${usd(data.totalAmount)}\n`;
  result += `You earned ${data.totalVolumeCredits} credits\n`;
  return result;

  function usd(aNumber) {
    return new Intl.NumberFormat("en-US",
                          { style: "currency", currency: "USD",
                            minimumFractionDigits: 2 }).format(aNumber/100);
  }
}

console.log(statement(invoices[0], plays))
