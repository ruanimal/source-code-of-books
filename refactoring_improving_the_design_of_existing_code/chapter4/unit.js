var buf = ['', '', '', '']
const describe = (desc, fn) => {
  for (let i=0; i<buf.length; i++) {
    buf[i] = ''
  }
  buf[0] = desc
  fn()
}

function it(msg, fn){
  buf[1] = msg
  fn()
  console.log(`${buf[0]}:${buf[1]} -> ${buf[2]}`)
  if (buf[3]) {
    console.log('\t' + buf[3])
  }
  for (let i=1; i<buf.length; i++) {
    buf[i] = ''
  }
}

function equal(exp, assertion) {
  if (exp === assertion) {
    buf[2] = 'succ'
  } else {
    buf[2] = 'fail'
    buf[3] = `${exp} is not equal ${assertion}`
  }
}

function expect(exp) {
  return {
    toBe: (assertion) => equal(exp, assertion)
  }
}

const assert = {
  equal: equal
}

function adder(a, b) {
  return a + b
}

describe('adder', () => {
  it('adds two numbers', () => {
    const result = adder(1, 2)
    expect(result).toBe(3)
    assert.equal(result, 3)
  })
  it('adds two numbers2', () => {
    const result = adder(2, 2)
    expect(result).toBe(3)
    assert.equal(result, 3)
  })
})

module.exports = {
  describe,
  expect,
  it,
}
