---
records:
    - id: QTJXVRFFB3
      kind: monograph
      title: Analysis I
      creators:
        - name: Roger Godement
          role: author
      date: "2004"
      msc:
        - code: 26-01
          from: zbmath_search
        - code: 00A05
          from: zbmath_search
        - code: 42-01
          from: zbmath_search
        - code: 30-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2004"
          ids:
            doi: 10.1007/978-3-642-18491-8
            zbl: "1096.26001"
            zbl_id: "2012130"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2004"
              ids:
                isbn:
                    - "9783540059233"
                    - "9783642184918"
              access:
                class: record
      relations:
        - kind: part_of
          to: W0CC03QJC7
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 dev scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-642-18491-8
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "2012130"
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
