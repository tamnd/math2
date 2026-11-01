---
records:
    - id: KPDFA3ZZRM
      kind: course-material
      title: 'Lecture 24b: Quiz 2 review'
      date: "2010"
      expressions:
        - key: e1
          kind: edition
          label: 2nd edition
          language: en
          date: "2010"
          manifestations:
            - key: m1
              kind: page
              publisher: MIT OpenCourseWare
              date: "2010"
              ids:
                ocw: 18-06-linear-algebra-spring-2010/resources/lecture-24b-quiz-2-review
              access:
                class: record
      relations:
        - kind: part_of
          to: GE3WH5EF6G/e1
          source: cluster/1
      scope:
        value: in
        rule: S6
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: ocw
          snapshot: blake3:ab57e74d727dbbb8cc6f30102b1562b267a6d76a54ffa725885e5e4ddfbb57b8
          native_id: 18-06-linear-algebra-spring-2010/resources/lecture-24b-quiz-2-review
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
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.14 scope/1
          note: from deferred to in
    - id: KPDP1QKBPV
      kind: monograph
      title: Beginner’s Course in Topology
      creators:
        - name: Dmitrij Borisovich Fuks
          role: author
        - name: Vladimir Abramovich Rokhlin
          role: author
        - name: Andrei Iacob
          role: author
      date: "1984"
      msc:
        - code: 54-01
          from: zbmath_search
        - code: 55-01
          from: zbmath_search
        - code: 57-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1984"
          ids:
            doi: 10.1007/978-3-642-61755-3
            zbl: "0562.54003"
            zbl_id: "3895865"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1984"
              ids:
                isbn:
                    - "9783540135777"
                    - "9783642617553"
              access:
                class: record
      relations:
        - kind: part_of
          to: W0CC03QJC7
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-642-61755-3
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "3895865"
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
