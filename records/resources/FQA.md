---
records:
    - id: FQADHCDNQX
      kind: monograph
      title: 'Steps into Analytic Number Theory: A Problem-Based Introduction'
      creators:
        - name: Paul Pollack
          role: author
        - name: Akash Singha Roy
          role: author
      date: "2021"
      msc:
        - code: 11-01
          from: zbmath_search
        - code: 11Mxx
          from: zbmath_search
        - code: 00A07
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2021"
          ids:
            doi: 10.1007/978-3-030-65077-3
            zbl: "1457.11002"
            zbl_id: "7301646"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2021"
              ids:
                isbn:
                    - "9783030650766"
                    - "9783030650773"
              access:
                class: record
      relations:
        - kind: part_of
          to: AQAR17SPHM
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.17 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-030-65077-3
          level: work
        - source: zbmath_search
          snapshot: blake3:ba52b67aca79888bd54f4ac0d57bd446df8c82ca03dd9e92e0bc9db1402905ce
          native_id: "7301646"
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
