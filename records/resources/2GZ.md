---
records:
    - id: 2GZSQHVRF7
      kind: course
      title: Introduction to Algebraic Geometry and Commutative Algebra
      creators:
        - name: Dilip P. Patil
          role: instructor
      date: "2019-12-16"
      msc:
        - code: 14-XX
          from: classify/1@2b838f8bc9d8
      ids:
        course: 04dese585:111108136
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2019-12-16"
          structure: 2GZSQHVRF7/e1.json
          manifestations:
            - key: m1
              kind: page
              publisher: IISc Bangalore
              ids:
                nptel: "111108136"
              access:
                class: record
            - key: m2
              kind: page
              date: "2019-12-16"
              ids:
                nptel: "111108136"
              access:
                class: record
      scope:
        value: in
        rule: S6
        by: m2 dev scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111108136"
          level: manifestation
        - source: nptel_video
          snapshot: blake3:7980ec84cfbca0f71922ec2d4e56d2385fa22a44c9cd025088eefbf06b61009d
          native_id: "111108136"
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
