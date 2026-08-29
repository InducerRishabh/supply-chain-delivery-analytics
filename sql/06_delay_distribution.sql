SELECT
    (
        "Days for shipping (real)"
        - "Days for shipment (scheduled)"
    ) AS shipping_delay_days,

    COUNT(*) AS delivery_records,

    ROUND(
        100.0 * COUNT(*) /
        SUM(COUNT(*)) OVER (),
        2
    ) AS pct_of_delivery_records,

    SUM(
        CASE
            WHEN "Delivery Status" = 'Late delivery'
            THEN 1
            ELSE 0
        END
    ) AS late_deliveries

FROM read_csv_auto(
    'data/DataCoSupplyChain_UTF8.csv'
)

WHERE "Delivery Status" IN (
    'Advance shipping',
    'Late delivery',
    'Shipping on time'
)

GROUP BY shipping_delay_days

ORDER BY shipping_delay_days;