---
records:
    - id: Y6M9MYS338
      kind: course-material
      title: 'Lecture 21: Eigenvalues and eigenvectors'
      date: "2010"
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2010"
          manifestations:
            - key: m1
              kind: page
              publisher: MIT OpenCourseWare
              date: "2010"
              ids:
                ocw: 18-06-linear-algebra-spring-2010/resources/lecture-21-eigenvalues-and-eigenvectors
              access:
                class: record
      relations:
        - kind: part_of
          to: GE3WH5EF6G/e1
          source: cluster/1
      scope:
        value: deferred
        until: "2027-01-30"
        reason: the classifier score 0.969 is in the middle band
        rule: S8
        by: classify/1@2b838f8bc9d8
      catalogue:
        - source: ocw
          snapshot: blake3:ab57e74d727dbbb8cc6f30102b1562b267a6d76a54ffa725885e5e4ddfbb57b8
          native_id: 18-06-linear-algebra-spring-2010/resources/lecture-21-eigenvalues-and-eigenvectors
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
          at: "2026-11-01"
          by: classify/1@2b838f8bc9d8
          note: from deferred to deferred
    - id: Y6MQ86K0X5
      kind: problem-set
      title: Putnam 1994
      creators:
        - name: Mathematical Association of America
          role: author
      date: "1994"
      msc:
        - code: 00A07
          from: putnam
        - code: 97U40
          from: putnam
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1994"
          structure: Y6MQ86K0X5/e1.json
      relations:
        - kind: part_of
          to: TYDZDDC2MA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: putnam
          snapshot: blake3:a8efce689e279311a280a90aaaac925d4b96f7c8ccdd9eb1e8fb29b48d574603
          native_id: "1994"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
