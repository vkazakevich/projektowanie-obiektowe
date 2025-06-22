const express = require('express')

require('dotenv').config()

const app = express()
const port = process.env.PORT || 4242

app.use(express.json())

const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY)

app.post('/payment-sheet', async (req, res) => {
  const amount = parseFloat(req.body.amount)
  const customer = await stripe.customers.create()

  const ephemeralKey = await stripe.ephemeralKeys.create(
    { customer: customer.id },
    { apiVersion: '2025-05-28.basil' }
  )

  const paymentIntent = await stripe.paymentIntents.create({
    amount: amount * 100.00,
    currency: 'eur',
    customer: customer.id,
    automatic_payment_methods: {
      enabled: true
    }
  })

  res.json({
    paymentIntent: paymentIntent.client_secret,
    ephemeralKey: ephemeralKey.secret,
    customer: customer.id,
    publishableKey: process.env.STRIPE_PUBLISHABLE_KEY
  })
})

app.listen(port, () => {
  console.log(`Server is running on port ${port}`)
})
