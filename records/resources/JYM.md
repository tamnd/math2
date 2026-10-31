---
records:
    - id: JYMXY87FXT
      kind: course
      title: Statistical Inference
      creators:
        - name: Somesh Kumar
          role: instructor
      ids:
        course:
            - 03w5sq511:111105043
            - 03w5sq511:111105124
      expressions:
        - key: e1
          kind: edition
          language: en
          manifestations:
            - key: m1
              kind: page
              publisher: IIT Kharagpur
              ids:
                nptel: "111105043"
            - key: m2
              kind: page
              publisher: IIT Kharagpur
              ids:
                nptel: "111105124"
      scope:
        value: deferred
        until: "2027-01-29"
        reason: no test decides the record, and the classifier has no model
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111105043"
          level: manifestation
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111105124"
          level: manifestation
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to deferred
---
