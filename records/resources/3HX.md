---
records:
    - id: 3HX92X2H1D
      kind: course
      title: Advanced Matrix Theory and Linear Algebra for Engineers
      creators:
        - name: Vittal Rao
          role: instructor
      date: "2012-06-18"
      msc:
        - code: 15-XX
          from: classify/1@2b838f8bc9d8
      ids:
        course: 04dese585:111108066
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2012-06-18"
          structure: 3HX92X2H1D/e1.json
          manifestations:
            - key: m1
              kind: page
              publisher: IISc Bangalore
              ids:
                nptel: "111108066"
              access:
                class: record
            - key: m2
              kind: page
              date: "2012-06-18"
              ids:
                nptel: "111108066"
              access:
                class: record
      scope:
        value: in
        rule: S6
        by: m2 dev scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111108066"
          level: manifestation
        - source: nptel_video
          snapshot: blake3:7980ec84cfbca0f71922ec2d4e56d2385fa22a44c9cd025088eefbf06b61009d
          native_id: "111108066"
          level: manifestation
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to deferred
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.4 scope/1
          note: from deferred to in
---
