---
records:
    - id: ZSY2EZRPJ2
      kind: course-material
      title: Exam 3 solutions
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
                ocw: 18-06-linear-algebra-spring-2010/resources/mit18_06s10_exam3_s10_soln
              access:
                class: record
      relations:
        - kind: part_of
          to: GE3WH5EF6G/e1
          source: cluster/1
      scope:
        value: deferred
        until: "2027-01-29"
        reason: no test decides the record, and the classifier has no model
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: ocw
          snapshot: blake3:ab57e74d727dbbb8cc6f30102b1562b267a6d76a54ffa725885e5e4ddfbb57b8
          native_id: 18-06-linear-algebra-spring-2010/resources/mit18_06s10_exam3_s10_soln
          level: manifestation
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to deferred
    - id: ZSYHG39EVZ
      kind: monograph
      title: Cauchy Problem for Differential Operators with Double Characteristics
      creators:
        - name: Tatsuo Nishitani
          role: author
      date: "2017"
      msc:
        - code: 35-02
          from: zbmath_search
        - code: 35L15
          from: zbmath_search
        - code: 35L30
          from: zbmath_search
        - code: 35R30
          from: zbmath_search
        - code: 35S10
          from: zbmath_search
        - code: 35A27
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2017"
          ids:
            doi: 10.1007/978-3-319-67612-8
            zbl: "1400.35001"
            zbl_id: "6783948"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2017"
              ids:
                isbn:
                    - "9783319676111"
                    - "9783319676128"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-67612-8
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "6783948"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
